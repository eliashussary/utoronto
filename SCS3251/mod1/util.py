from IPython.display import HTML, display

def list_to_html_table(l):
    return display(HTML(
    '<table><tr>{}</tr></table>'.format(
        '</tr><tr>'.join(
            '<td>{}</td>'.format('</td><td>'.join(str(_) for _ in row)) for row in l)
        )
    ))