import jmake

jmake.setupenv()

workspace = jmake.Workspace('imgui')

# we need the header files to compile the glfw backend
glfw = jmake.package('glfw', 'https://github.com/DanDanCool/glfw')
imgui = jmake.Project('imgui', jmake.Target.STATIC_LIBRARY)

files = jmake.glob('.', ['*.h', '*.cpp'])
files.extend(jmake.fullpath([
    'backends/imgui_impl_glfw.h',
    'backends/imgui_impl_glfw.cpp',
    'backends/imgui_impl_opengl3.h',
    'backends/imgui_impl_opengl3.cpp',
    'backends/imgui_impl_opengl3_loader.h',
    'backends/imgui_impl_dx11.h',
    'backends/imgui_impl_dx11.cpp',
    'backends/imgui_impl_dx12.h',
    'backends/imgui_impl_dx12.cpp'
    ]))

imgui.add(files)

host = jmake.Host()
imgui.include(jmake.fullpath('.') + jmake.rootpath(f'{host.lib}/glfw/include'))
imgui.export(includes=jmake.fullpath('.'))

debug = imgui.filter('debug')
debug['debug'] = True

workspace.add(imgui)

jmake.generate(workspace)
