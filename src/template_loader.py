from jinja2 import Environment, FileSystemLoader


class TemplateLoader:
    @staticmethod
    def load_template(template_name, template_path='templates') -> Environment:
        file_loader = FileSystemLoader(template_path)
        env = Environment(loader=file_loader)
        return env.get_template(template_name)
