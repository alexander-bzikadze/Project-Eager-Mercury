import sublime, sublime_plugin, os

from importlib.machinery import SourceFileLoader
ct = SourceFileLoader("CorrectnessTests", os.path.join(sublime.packages_path(), "User", "correctnessTests.py")).load_module()
ir = SourceFileLoader("InfoReader", os.path.join(sublime.packages_path(), "User", "infoReader.py")).load_module()

extension = ".pem"

class GetFilesCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		info = ir.InfoReader()
		cT = ct.CorrectnessTests()
		cT.infoFileExistence()

		if cT.projectSelection():
			print("Project is not selected.")
			return 0
		if cT.projectFileExistence(info.getCurrentProject(), info.getCurrentProjectPath()):
			print("Project file not found or it is empty.")
			return 0
		if cT.projectFileCorrectness(info.getCurrentProject(), info.getCurrentProjectPath()):
			print("Project file is not correct.")
			return 0

		projectPath = os.path.join(info.getCurrentProjectPath(), info.getCurrentProject() + extension)
		projectFile = open(projectPath, 'r')
		lines = projectFile.readlines()
		projectFile.close()
		for i in range(lines.index("source:\n") + 1, len(lines)):
			print(lines[i][0 : len(lines[i]) - 1])