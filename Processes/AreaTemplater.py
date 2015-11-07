import os
import re
import shutil


class AreaTemplater:
    def __init__(self, path, area):
        self.path = path;
        self.area = area;

    def process_area(self):
        self.create_service();
        self.create_area();

    def create_service(self):
        service_path = (self.path if self.path.endswith('/') else self.path + '/') + 'SIFSE.Services/' + self.area.name;
        shutil.rmtree(service_path, True);
        os.makedirs(service_path);
        self.create_service_file(service_path);

    def create_service_file(self, service_path):
        file_name = self.area.name + 'Service.cs';
        temp_path = service_path + '/' + file_name;
        with open(temp_path, 'w') as f:
            file_code = self.get_service_code();
            f.write(file_code);
        f.close();

    def get_service_code(self):
        file_name = 'Service.cs';
        temp_path = './Templates/' + file_name;
        code = '';
        with open(temp_path, 'r') as f:
            code = f.read();
        f.close();
        code = re.sub(r'\$area\$', self.area.name, code);
        return code;

    def create_area(self):
        pass;