import socket
import urllib.request
import os
import datetime
import logging
# logging setup
logging.basicConfig(filename="../log/odoo_download.log", format='%(asctime)s %(message)s', filemode='a')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def main():
    version_list = ['15.0', '16.0', '17.0', ]
    date = datetime.datetime.now().date().strftime('%Y%m%d')

    for version_no in version_list:
        socket.setdefaulttimeout(5)
        download_path = '../downloads'
        # download_path = '/var/www/html/downloads'  # you can use a webserver like nginx to share downloads
        try:
            # url = f'https://nightly.odoo.com/{version_no}/nightly/deb/odoo_{version_no}.{date}_all.deb '
            url = f'http://myhome.gilaneh.com:81/ddd/d.txt'
            filename = f'odoo_{version_no}.{date}_all.deb'
            path_filename = os.path.join(download_path, filename)
            for index in range(1, 1000):
                if os.path.exists(path_filename):
                    filename = f'odoo_{version_no}.{date}_all_{index}.deb'
                    path_filename = os.path.join(download_path, filename)
                else:
                    break
            urllib.request.urlretrieve(url, path_filename)
            logger.info(f'Date: {date} filename: {path_filename}')
        except Exception as err:
            logger.error(err)


if __name__ == '__main__':
    main()
