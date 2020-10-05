import cgi
import sys
import codecs
import os
import http.cookies
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

form = cgi.FieldStorage()
f_name = form.getfirst("f_name", "off")
l_name = form.getfirst("l_name", "off")
field_1 = form.getfirst("field_1", "off")
field_2 = form.getfirst("field_2", "off")
field_3 = form.getfirst("field_3", "off")
field_4 = form.getfirst("field_4", "off")

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Data form!</title>
        </head>
        <body>""")

print("<h1>Data form!</h1>")
print("<p>First Name: {}</p>".format(f_name))
print("<p>Last Name: {}</p>".format(l_name))
print("<p>English: {}</p>".format(field_1))
print("<p>German: {}</p>".format(field_2))
print("<p>Math: {}</p>".format(field_3))
print("<p>Biology: {}</p>".format(field_4))

print("""</body>
        </html>""")


hit_count_path = os.path.join(os.path.dirname(__file__), "submit-count.txt")

if os.path.isfile(hit_count_path):
    with open(hit_count_path) as fp:
        hit_count_str = fp.read()
        try:
            hit_count = int(hit_count_str)
        except ValueError:
            hit_count = 0
    hit_count += 1
else:
    hit_count = 1

with open(hit_count_path, 'w') as fp:
    fp.write(str(hit_count))



response = """
  <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="utf-8">
    </head>
    <body>
      <p>
        Number of submits: {0}
      </p>
    </body>
  </html>
""".format(cgi.escape(str(hit_count)))

print(response)


