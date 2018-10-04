import sublime
import sublime_plugin


class WatchWordCountCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        print('TEST')
        # self.view.insert(edit, 0, "Hello, World!")
        sublime.set_clipboard(' - '.join(repr(e) for e in sublime.windows()))
        for e in sublime.windows():
            print(e)
        # w = sublime.active_window()
        out = self.window.create_output_panel('WatchWordCount')
        out.insert(edit, 0, 'Hello, World!')
        print('test')