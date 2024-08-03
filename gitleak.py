import json

# Load the JSON data
with open('./gitleaks-report.json') as f:
    data = json.load(f)

# Create the HTML table with enhanced CSS
html = """
<!DOCTYPE html>
<html>
<head>
<style>
    body {
        font-family: Arial, sans-serif;
    }
    table {
        width: 100%;
        border-collapse: collapse;
    }
    table, th, td {
        border: 1px solid #ddd;
    }
    th, td {
        padding: 8px;
        text-align: left;
    }
    th {
        background-color: #f2f2f2;
        color: black;
    }
    tr:nth-child(even) {
        background-color: #f9f9f9;
    }
    tr:hover {
        background-color: #f1f1f1;
    }
    .container {
        margin: 20px;
    }
</style>
</head>
<body>

<div class="container">
<h2>Gitleaks Report</h2>
<table>
<tr>
    <th>Description</th>
    <th>StartLine</th>
    <th>EndLine</th>
    <th>StartColumn</th>
    <th>EndColumn</th>
    <th>Match</th>
    <th>Secret</th>
    <th>File</th>
    <th>SymlinkFile</th>
    <th>Commit</th>
    <th>Entropy</th>
    <th>Author</th>
    <th>Email</th>
    <th>Date</th>
    <th>Message</th>
    <th>Tags</th>
    <th>RuleID</th>
    <th>Fingerprint</th>
</tr>
"""

for item in data:
    html += f"""
    <tr>
        <td>{item.get('Description', '')}</td>
        <td>{item.get('StartLine', '')}</td>
        <td>{item.get('EndLine', '')}</td>
        <td>{item.get('StartColumn', '')}</td>
        <td>{item.get('EndColumn', '')}</td>
        <td>{item.get('Match', '')}</td>
        <td>{item.get('Secret', '')}</td>
        <td>{item.get('File', '')}</td>
        <td>{item.get('SymlinkFile', '')}</td>
        <td>{item.get('Commit', '')}</td>
        <td>{item.get('Entropy', '')}</td>
        <td>{item.get('Author', '')}</td>
        <td>{item.get('Email', '')}</td>
        <td>{item.get('Date', '')}</td>
        <td>{item.get('Message', '')}</td>
        <td>{', '.join(item.get('Tags', []))}</td>
        <td>{item.get('RuleID', '')}</td>
        <td>{item.get('Fingerprint', '')}</td>
    </tr>
    """

html += """
</table>
</div>

</body>
</html>
"""

# Save the HTML to a file
with open('./gitleaks-report.html', 'w') as f:
    f.write(html)

print("HTML file created successfully.")
