// 指定输入路径
fis.config.set('project.include', ['templates/**', 'static/**']);
// 忽略无需参与编译的文件
fis.config.set('project.exclude', ['static/**.less']);