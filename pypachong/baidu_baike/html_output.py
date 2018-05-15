class Output(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, new_data):
       if new_data is None:
        return
       self.datas.append(new_data)


    def output_html(self):
        fout=open("output.html","w")
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        for datas in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>"%datas['url'])
            fout.write("<td>%s</td>"%datas['title'])
           #fout.write("<td>%s</td>"%datas['summary'])
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")


        fout.close()