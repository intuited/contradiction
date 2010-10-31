"""waf script to build the README file from the template.

Requires that the module `help_template`_ be installed.

.. _help_template: http://github.com/intuited/help_template
"""
def configure(conf):
    pass

def build(bld):
    def build_readme(task):
        import help_template
        template_text = task.inputs[0].read()
        template = help_template.HelpTemplate(template_text)
        task.outputs[0].write(template.substitute())
    
    bld(rule=build_readme,
        source='README.template contradiction.py',
        target='../README.txt')
