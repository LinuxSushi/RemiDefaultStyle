def default_style(element, style):
    old_init = getattr(element, "__init__")
    def new_init(self, *args, **kwargs):
        old_init(self, *args, **kwargs)
        self.set_style(style)
    setattr(element, '__init__', new_init)

def default_styles(elements):
    for element, style in elements.items():
        default_style(element, style)