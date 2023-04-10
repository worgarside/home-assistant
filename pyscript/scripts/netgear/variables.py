"""Update a whole load of variables from the Netgear API"""
from __future__ import annotations

from collections.abc import Callable
from datetime import timedelta
from json import dumps
from socket import gethostname
from typing import Any

from helpers import HAExceptionCatcher, get_secret
from pynetgear import Netgear

MODULE_NAME = "netgear"

if gethostname() != "homeassistant":
    from helpers import local_setup  # pylint: disable=ungrouped-imports

    log, task, sync_mock, decorator, decorator_with_args = local_setup()
    persistent_notification = sync_mock
    var = sync_mock
    mqtt = sync_mock
    pyscript_executor = decorator
    service = decorator
    time_trigger: Callable[[Any], Callable[..., Any]] = decorator_with_args


PASSWORD = get_secret("password", module=MODULE_NAME)
NIGHTHAWK = Netgear(password=PASSWORD, host="10.0.0.1", user="admin")

RESPONSE_KEY_VARIABLE_MAPPING = {
    "ModelName": "var.netgear_r8000_model_name",
    "Description": "var.netgear_r8000_description",
    "SerialNumber": "var.netgear_r8000_serial_number",
    "Firmwareversion": "var.netgear_r8000_firmware_version",
    "SmartAgentversion": "var.netgear_r8000_smart_agent_version",
    "FirewallVersion": "var.netgear_r8000_firewall_version",
    "VPNVersion": "var.netgear_r8000_vpn_version",
    "OthersoftwareVersion": "var.netgear_r8000_other_software_version",
    "Hardwareversion": "var.netgear_r8000_hardware_version",
    "Otherhardwareversion": "var.netgear_r8000_other_hardware_version",
    "FirstUseDate": "var.netgear_r8000_first_use_date",
    "DeviceName": "var.netgear_r8000_device_name",
    "FirmwareDLmethod": "var.netgear_r8000_firmware_dl_method",
    "FirmwareLastUpdate": "var.netgear_r8000_firmware_last_update",
    "FirmwareLastChecked": "var.netgear_r8000_firmware_last_checked",
    "DeviceMode": "var.netgear_r8000_device_mode",
    "NewTodayConnectionTime": "var.netgear_r8000_today_connection_time",
    "NewTodayUpload": "var.netgear_r8000_today_upload",
    "NewTodayDownload": "var.netgear_r8000_today_download",
    "NewYesterdayConnectionTime": "var.netgear_r8000_yesterday_connection_time",
    "NewYesterdayUpload": "var.netgear_r8000_yesterday_upload",
    "NewYesterdayDownload": "var.netgear_r8000_yesterday_download",
    "NewWeekConnectionTime": "var.netgear_r8000_week_connection_time",
    "NewMonthConnectionTime": "var.netgear_r8000_month_connection_time",
    "NewLastMonthConnectionTime": "var.netgear_r8000_last_month_connection_time",
    "NewWeekUploadTotal": "var.netgear_r8000_week_upload_total",
    "NewWeekUploadAverage": "var.netgear_r8000_week_upload_average",
    "NewWeekDownloadTotal": "var.netgear_r8000_week_download_total",
    "NewWeekDownloadAverage": "var.netgear_r8000_week_download_average",
    "NewMonthUploadTotal": "var.netgear_r8000_month_upload_total",
    "NewMonthUploadAverage": "var.netgear_r8000_month_upload_average",
    "NewMonthDownloadTotal": "var.netgear_r8000_month_download_total",
    "NewMonthDownloadAverage": "var.netgear_r8000_month_download_average",
    "NewLastMonthUploadTotal": "var.netgear_r8000_last_month_upload_total",
    "NewLastMonthUploadAverage": "var.netgear_r8000_last_month_upload_average",
    "NewLastMonthDownloadTotal": "var.netgear_r8000_last_month_download_total",
    "NewLastMonthDownloadAverage": "var.netgear_r8000_last_month_download_average",
    "CurrentVersion": "var.netgear_r8000_current_firmware_version",
    "NewVersion": "var.netgear_r8000_new_firmware_version",
    "ReleaseNote": "var.netgear_r8000_firmware_release_note",
    "NewCPUUtilization": "var.netgear_r8000_cpu_utilization",
    "NewPhysicalMemory": "var.netgear_r8000_physical_memory",
    "NewMemoryUtilization": "var.netgear_r8000_memory_utilization",
    "NewPhysicalFlash": "var.netgear_r8000_physical_flash",
    "NewAvailableFlash": "var.netgear_r8000_available_flash",
    "NewEthernetLinkStatus": "var.netgear_r8000_ethernet_link_status",
    "NewEnable": "var.netgear_r8000_enable",
    "NewConnectionType": "var.netgear_r8000_connection_type",
    "NewExternalIPAddress": "var.netgear_r8000_external_ip_address",
    "NewSubnetMask": "var.netgear_r8000_subnet_mask",
    "NewAddressingType": "var.netgear_r8000_addressing_type",
    "NewDefaultGateway": "var.netgear_r8000_default_gateway",
    "NewMACAddress": "var.netgear_r8000_mac_address",
    "NewMACAddressOverride": "var.netgear_r8000_mac_address_override",
    "NewMaxMTUSize": "var.netgear_r8000_max_mtu_size",
    "NewDNSEnabled": "var.netgear_r8000_dns_enabled",
    "NewDNSServers": "var.netgear_r8000_dns_servers",
    "NewOOKLAUplinkBandwidth": "var.netgear_r8000_uplink_bandwidth",
    "NewOOKLADownlinkBandwidth": "var.netgear_r8000_downlink_bandwidth",
    "AveragePing": "var.netgear_r8000_average_ping",
}


def update_variables(method_name: str, new_variables: dict[str, object]) -> None:
    """Update variable values with a fresh response

    Args:
        method_name (str): The name of the method that was called
        new_variables (dict[str, object]): The new variables to set, from a response
            from the Netgear router
    """

    for k, v in new_variables.items():
        with HAExceptionCatcher(MODULE_NAME, f"update_variable('{k}')"):
            if (var_name := RESPONSE_KEY_VARIABLE_MAPPING.get(k)) is not None:
                if isinstance(v, timedelta):
                    v = v.total_seconds()

                if isinstance(v, float):
                    v = round(v, 2)

                var.set(
                    entity_id=var_name,
                    value=v,
                    force_update=True,
                )
            else:
                log.info(
                    "New key found in `%s` response: `%s`. Full response:\n%s",
                    method_name,
                    k,
                    dumps(new_variables, default=str),
                )
                persistent_notification.create(
                    title="New key found in `NETGEAR.get_info` response",
                    message=f"`{k}`. Full response:\n"
                    f"```{dumps(new_variables, default=repr)}```",
                )


@time_trigger("cron(5 0 * * *)")
def netgear_get_info() -> None:
    """Get info from Netgear router

    - ModelName
    - DeviceName
    - SerialNumber
    - FirmwareVersion
    - FirewallVersion
    - HardwareVersion
    - FirmwareLastUpdate
    - FirmwareLastChecked
    """
    info = task.executor(NIGHTHAWK.get_info)

    update_variables("get_info", info)


@time_trigger("cron(*/15 * * * *)")
def netgear_get_traffic_meter() -> None:
    """Get traffic meter info from Netgear router

    - NewTodayConnectionTime
    - NewTodayUpload
    - NewTodayDownload
    - NewYesterdayConnectionTime
    - NewYesterdayUpload
    - NewYesterdayDownload
    - NewWeekConnectionTime
    - NewWeekUpload
    - NewWeekDownload
    - NewMonthConnectionTime
    - NewMonthUpload
    - NewMonthDownload
    - NewLastMonthConnectionTime
    - NewLastMonthUpload
    - NewLastMonthDownload
    """
    traffic_meter = task.executor(NIGHTHAWK.get_traffic_meter)

    for key in (
        "NewWeekUpload",
        "NewWeekDownload",
        "NewMonthUpload",
        "NewMonthDownload",
        "NewLastMonthUpload",
        "NewLastMonthDownload",
    ):
        total, average = traffic_meter.pop(key, [None, None])
        traffic_meter[key + "Total"] = total
        traffic_meter[key + "Average"] = average

    update_variables("get_traffic_meter", traffic_meter)


@time_trigger("cron(5 0 * * *)")
def netgear_check_new_firmware() -> None:
    """Check for new firmware

    - CurrentVersion
    - NewVersion
    - ReleaseNote
    """

    new_firmware = task.executor(NIGHTHAWK.check_new_firmware)

    update_variables("check_new_firmware", new_firmware)


# @time_trigger("cron(* * * * *)")
def netgear_get_system_info() -> None:
    """Get system info from Netgear router

    - NewCPUUtilization
    - NewPhysicalMemory
    - NewMemoryUtilization
    - NewPhysicalFlash
    - NewAvailableFlash"""
    system_info = task.executor(NIGHTHAWK.get_system_info)

    update_variables("get_system_info", system_info)


# @time_trigger("cron(*/5 * * * *)")
def netgear_check_ethernet_link() -> None:
    """Check ethernet link

    - NewEthernetLinkStatus
    """
    ethernet_link_status = task.executor(NIGHTHAWK.check_ethernet_link)
    update_variables("check_ethernet_link", ethernet_link_status)


# @time_trigger("cron(*/15 * * *)")
def netgear_get_wan_ip_con_info() -> None:
    """Get WAN IP connection info

    - NewEnable
    - NewConnectionType
    - NewExternalIPAddress
    - NewSubnetMask
    - NewAddressingType
    - NewDefaultGateway
    - NewMACAddress
    - NewMACAddressOverride
    - NewMaxMTUSize
    - NewDNSEnabled
    - NewDNSServers
    """
    wan_ip_con_info = task.executor(NIGHTHAWK.get_wan_ip_con_info)

    update_variables("get_wan_ip_con_info", wan_ip_con_info)


# @time_trigger("cron(*/20 * * * *)")
def netgear_run_speed_test() -> None:
    """Get new speed test result

    - NewOOKLAUplinkBandwidth
    - NewOOKLADownlinkBandwidth
    - AveragePing"""
    new_speed_test_result = task.executor(NIGHTHAWK.get_new_speed_test_result)

    update_variables("get_new_speed_test_result", new_speed_test_result)
