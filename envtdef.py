"""
Sublime Text Plugin Idea
========================

- Create new $$\LaTeX$$ environment which is a copy of an existing one,
  but with default values
- if old envrionment had name `<envt>`, the new one would be named `<envt>def`
"""
import sublime
import sublime_plugin


class DefaultEnvironmentCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.insert(edit, 0, "Hello, World!")
