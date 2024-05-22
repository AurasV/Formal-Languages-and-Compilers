import pandas as pd


def create_html_table(csv_filepath):
    df = pd.read_csv(csv_filepath, usecols=['ID', 'FirstName', 'LastName', 'Email', 'Age'])
    html_table = df.to_html(index=False)
    css = """
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #DCDCDC;
            text-align: center;
            padding: 8px;
        }
        tr:nth-child(even) {
            background-color: #696969;
        }
    </style>
    """

    html_output = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <title>Table Output</title>
    {css}
    </head>
    <body>
    {html_table}
    </body>
    </html>
    """

    with open('output.html', 'w') as file:
        file.write(html_output)

    print("HTML file 'output.html' has been created with the striped table.")


if __name__ == "__main__":
    create_html_table('Lab7.csv')
