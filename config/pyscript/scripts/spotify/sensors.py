from os.path import isfile

from requests import get
from wg_utilities.functions import force_mkdir
from helpers import write_file


@state_trigger("sensor.spotify_matt_scott_media_album_artwork_internal_url")
@state_trigger("sensor.spotify_tom_jones_media_album_artwork_internal_url")
@state_trigger("sensor.spotify_will_garside_media_album_artwork_internal_url")
def save_album_artwork(var_name, value, old_value):
    """Saves the artwork for a given album to the local file storage for use elsewhere

    Args:
        var_name (str): the sensor which triggered this function
        value (str): the value of the sensor
        old_value (str): the previous value of the sensor
    """

    if value in ("unknown", old_value):
        return

    log.info("Triggered by `%s`", var_name)

    cleansed_album_name = ""
    for char in str(state.get(var_name.replace("_artwork_internal_url", "_name"))):
        if char.isalnum():
            cleansed_album_name += char.lower()

    cleansed_artist_name = ""
    for char in str(
        state.get(var_name.replace("_album_artwork_internal_url", "_artist"))
    ):
        if char.isalnum():
            cleansed_artist_name += char.lower()

    if isfile(
        target_path := "/".join(
            [
                "www",
                "album_artwork",
                cleansed_artist_name,
                f"{cleansed_album_name}.jpg",
            ]
        )
    ):
        return

    res = task.executor(get, f"http://{sensor.local_ip}:8123{value}")

    res.raise_for_status()

    log.info(
        "Album artwork endpoint response was `%s %s` - writing content to %s",
        res.status_code,
        res.reason,
        target_path,
    )

    write_file(
        force_mkdir(
            target_path,
            True,
        ),
        res.content,
        encoding=None,
    )
