import os
import shutil
import re
from Utils.RegexUtils import dollar_replace
from Utils.KivyConfNavConfig import get_config


class AreaTemplater:
    def __init__(self, path, area):
        self.path = path if path.endswith('/') else path + '/'
        self.area = area

    def prepare_dir(self, path):
        temp_path = self.path + path
        shutil.rmtree(temp_path, True)
        os.makedirs(temp_path)

    def process_area(self):
        self.create_model()
        self.create_service()
        self.create_area()

    def create_model(self):
        service_path = dollar_replace(get_config('Paths', 'Models'), {'area': self.area.name})
        self.prepare_dir(service_path)

    def create_service(self):
        service_path = dollar_replace(get_config('Paths', 'Services'), {'area': self.area.name})
        self.prepare_dir(service_path)
        self.create_service_file(service_path)

    def create_service_file(self, service_path):
        file_name = self.area.name + 'Service.cs'
        temp_path = self.path + service_path + '/' + file_name
        file_code = self.get_service_code()
        with open(temp_path, 'w') as f:
            f.write(file_code)
        f.close()

    def get_service_code(self):
        temp_path = './Templates/Service.cs'
        with open(temp_path, 'r') as f:
            code = f.read()
        f.close()
        code = dollar_replace(code, {'area': self.area.name})
        return code

    def create_area(self):
        for controller in self.area.controllers:
            self.create_controller(controller)
            self.create_view(controller)

    def create_controller(self, controller):
        controller_path = dollar_replace(get_config('Paths', 'Controllers'), {'area': self.area.name, 'controller': controller.name})
        self.prepare_dir(controller_path)
        self.create_controller_file(controller_path, controller)

    def create_controller_file(self, path, controller):
        temp_path = self.path + path + '/' + controller.name + 'Controller.cs'
        file_code = self.get_controller_code(controller)
        with open(temp_path, 'w') as f:
            f.write(file_code)
        f.close()

    def get_controller_code(self, controller):
        temp_path = './Templates/Controller.cs'
        with open(temp_path, 'r') as f:
            code = f.read()
        f.close()
        code = dollar_replace(code, {'area': self.area.name, 'controller': controller.name})
        action_code_regex = re.compile(r'(#region TemplateActions(.*)#endregion TemplateActions)', re.DOTALL)
        action_code_template = re.search(action_code_regex, code).group(2)
        action_code = ''
        for action in controller.actions:
            action_code += dollar_replace(action_code_template, {'action': action})
            action_code += '\n\n'
        code = re.sub(action_code_regex, action_code, code)
        return code

    def create_view(self, controller):
        view_path = dollar_replace(get_config('Paths', 'Views'), {'area': self.area.name, 'controller': controller.name})
        self.prepare_dir(view_path)
        for action in controller.actions:
            self.create_controller_view(view_path, action)

    def create_controller_view(self, path, action):
        temp_path = self.path + path + '/' + action + '.cshtml'
        file_code = self.get_view_code(action)
        with open(temp_path, 'w') as f:
            f.write(file_code)
        f.close()

    def get_view_code(self, action):
        temp_path = './Templates/View.cshtml'
        with open(temp_path, 'r') as f:
            code = f.read()
        f.close()
        code = dollar_replace(code, {'action': action})
        return code

