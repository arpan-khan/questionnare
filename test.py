import webbrowser
def generate_html_file(num_questions):
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Questionnaire</title>
        <link rel="stylesheet" type="text/css" href="style.css">
    </head>
    <body>
        <header>
            <h1>Questionnaire</h1>
        </header>
        <div class="container">
            <form>
    '''

    for i in range(1, num_questions + 1):
        html += '''
        <div class="question">
            <p>{0}. <ul class="options-list">
                <li><label><input type="radio" name="question{0}" value="A" /> A</label></li>
                <li><label><input type="radio" name="question{0}" value="B" /> B</label></li>
                <li><label><input type="radio" name="question{0}" value="C" /> C</label></li>
                <li><label><input type="radio" name="question{0}" value="D" /> D</label></li>
                <li><label><input type="radio" name="question{0}" value="E" /> E</label></li>
                <li><label><input type="radio" name="question{0}" value="Skip" /> Skip</label></li>
            </ul></p>
            <div class="options">
                <label>
                    <input type="checkbox" name="correct" value="correct" /> Correct
                </label>
                <label>
                    <input type="checkbox" name="incorrect" value="incorrect" /> Incorrect
                </label>
            </div>
        </div>
        '''.format(i)

    html += '''
            
            </form>
        </div>
    </body>
    </html>
    '''

    with open('questionnaire.html', 'w') as file:
        file.write(html)

    print('HTML file generated successfully.')
    
    webbrowser.open('questionnaire.html')

# Example usage
num_questions = int(input('Enter the number of questions: '))
generate_html_file(num_questions)
