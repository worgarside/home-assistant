ARG BUILD_FROM
FROM $BUILD_FROM

COPY yas_209_dlna_bridge /yas_209_dlna_bridge

# Install requirements for add-on
RUN \
  apk add --no-cache python3 python3 py3-pip py3-lxml

WORKDIR /yas_209_dlna_bridge

RUN echo $BUILD_FROM

RUN pip3 install -r requirements.txt
RUN pip3 install --no-deps -r requirements_no_deps.txt

# Copy data for add-on
COPY run.sh /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]