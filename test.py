import webbrowser

def generate_html_file(num_questions):
    html = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Questionnaire</title>
        <link rel="stylesheet" type="text/css" href="style.css">
        <script>
            function showResults() {{
                var correctCount = 0;
                var incorrectCount = 0;
                var skippedCount = 0;

                // Loop through questions to check answers
                for (var i = 1; i <= {num_questions}; i++) {{
                    var selectedOption = document.querySelector('input[name="question' + i + '"]:checked');
                    var isCorrect = document.getElementById('correct' + i).checked;

                    if (selectedOption) {{
                        if (isCorrect) {{
                            correctCount++;
                        }} else {{
                            incorrectCount++;
                        }}
                    }} else {{
                        skippedCount++;
                    }}
                }}

                // Display results in a popup
                alert('Correct: ' + correctCount + '\\nIncorrect: ' + incorrectCount + '\\nSkipped: ' + skippedCount);
            }}
        </script>
    </head>
    <body>
        <header>
            <h1>Questionnaire</h1>
        </header>
        <div class="container">
            <form onsubmit="showResults(); return false;">
    '''

    for i in range(1, num_questions + 1):
        html += f'''
        <div class="question">
            <label for="question{i}">{i}.</label>
            <ul class="options-list">
                <li><label><input type="radio" id="question{i}A" name="question{i}" value="A" /> A</label></li>
                <li><label><input type="radio" id="question{i}B" name="question{i}" value="B" /> B</label></li>
                <li><label><input type="radio" id="question{i}C" name="question{i}" value="C" /> C</label></li>
                <li><label><input type="radio" id="question{i}D" name="question{i}" value="D" /> D</label></li>
                <li><label><input type="radio" id="question{i}E" name="question{i}" value="E" /> E</label></li>
                <li><label><input type="radio" id="question{i}Skip" name="question{i}" value="Skip" /> Skip</label></li>
            </ul>
            <div class="options">
                <label>
                    <input type="checkbox" id="correct{i}" name="correct" value="correct" /> Correct
                </label>
                <label>
                    <input type="checkbox" id="incorrect{i}" name="incorrect" value="incorrect" /> Incorrect
                </label>
            </div>
        </div>
        '''

    html += '''
            <input type="submit" value="Submit">
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
