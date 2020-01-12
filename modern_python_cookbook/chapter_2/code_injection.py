import string

# the string.Formatter object allows you to extend its syntax and supports code injection

class TemplateFormatter(string.Formatter):
  def get_field(self, field_name, args, kwargs):
    if field_name.startswith('$'):
      code = field_name[1:]
      val = eval(code, {}, dict(kwargs)):
      return val, field_name
    else:
      return super(TemplateFormatter , self).get_field(field_name, args, kwargs)
