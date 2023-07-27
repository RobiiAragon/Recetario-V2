import jinja2
import pdfkit

def crea_pdf(ruta_template,info,rutacss=''):
    nombre_template = ruta_template.split('/')[-1]
    ruta_template = ruta_template.replace(nombre_template,'')

env = jinja2.Environment(loader=jinja2.FileSystemLoader(ruta_template))
template = env.get_template(nombre_template)
html = template.render(info)
print(html)

if __name__ == "__main__":
    ruta_template = 'APP\DEMO\template.html'
    info = {"nombreAlumno":"Jesus Aragon","nombreCurso":"python basico"}
    crea_pdf(ruta_template,info)