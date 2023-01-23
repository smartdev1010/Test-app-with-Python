txt_file = input("Enter txt file:")
f = open(txt_file, 'r')
title = f.readline()
sub_title = f.readline()
file_name = f.readline()

title = title.split('\n')[0]
sub_title = sub_title.split('\n')[0]
file_name = file_name.split('\n')[0]

f1 = open(str(file_name) + '.html', 'w')
f2 = open(str(file_name) + '.js', 'w')


class myProblem:
    def __init__(self, p_text, p_answer):
        self.text = p_text
        self.answers = p_answer


content = f.read()
content = ''.join(content.split("\n"))
tmp_problems = content.split("</rb>")
problems = []
result_problems = []
for i in range(len(tmp_problems) - 1):
    tmp_problems[i] += "</rb>"

for problem in tmp_problems:
    problem = problem.split("</cb>")
    if len(problem) > 0:
        for i in range(len(problem) - 1):
            problem[i] += "</cb>"
    problems += problem
f2.write("let data = [\n")
for problem in problems:
    problem_type = 0
    problem = problem.split('<rb>')
    if len(problem) > 1:
        problem = problem[1]
    else:
        problem = problem[0]
    problem = problem.split('</rb>')[0]
    problem = problem.split('<cb>')
    if len(problem) > 1:
        problem = problem[1]
        problem_type = 1
    else:
        problem = problem[0]
    problem = problem.split('</cb>')[0]
    problem = problem.split('</q>')
    if len(problem) > 1:
        problem[0] = problem[0].split('<q>')[1]
        problem[1] = problem[1].split('</ans>')
        problem[1].pop()
        for i in range(len(problem[1])):
            problem[1][i] = problem[1][i].split('<ans>')[1]
        mp = myProblem(problem[0], problem[1])
        result_problems.append(mp)
        f2.write("{ type: " + str(problem_type) + ", problem: '" +
                 str(problem[0]) + "', \n answers: [")
        for i in mp.answers:
            f2.write("'" + i + "',")
        f2.write("]},\n")
f2.write("];\n")
f2.writelines("\n".join(["let orders = [];",
                         "let testMethod = 0;",
                         "let score = 0;",
                         "let problemNo = 0;",
                         "let flag = 0;",
                         "document.getElementById('numbers').innerHTML = data.length;",
                         "function goTwoStage() {",
                         "  problemNo++;",
                         "  if (document.getElementsByName('my_radio')[0].checked) {",
                         "    testMethod = 1;",
                         "  } else if (document.getElementsByName('my_radio')[1].checked) {",
                         "    testMethod = 2;",
                         "  } else if (document.getElementsByName('my_radio')[2].checked) {",
                         "    testMethod = 3;",
                         "  }",
                         "  if (testMethod && $('#problems').val() <= data.length && $('#player').val()) {",
                         "    $('#one').parent().removeClass('invalid');",
                         "    $('#problems').removeClass('invalid');",
                         "    $('#player').removeClass('invalid');",
                         "    if (testMethod == 1) {",
                         "      for (let index = 0; index < data.length; index++) {",
                         "        let order = {};",
                         "        order.id = index;",
                         "        order.answers = [];",
                         "        for (let index1 = 0; index1 < data[index].answers.length; index1++)",
                         "          order.answers.push(index1);",
                         "        orders.push(order);",
                         "      }",
                         "    } else if (testMethod == 2) {",
                         "      for (let index = 0; index < data.length; index++) {",
                         "        let order = {};",
                         "        order.id = index;",
                         "        order.answers = [];",
                         "        for (let index1 = 0; index1 < data[index].answers.length; index1++)",
                         "          order.answers.push(index1);",
                         "        orders.push(order);",
                         "      }",
                         "      for (var i = orders.length - 1; i > 0; i--) {",
                         "        var j = Math.floor(Math.random() * (i + 1));",
                         "        var temp = orders[i];",
                         "        orders[i] = orders[j];",
                         "        orders[j] = temp;",
                         "      }",
                         "    } else if (testMethod == 3) {",
                         "      for (let index = 0; index < data.length; index++) {",
                         "        let order = {};",
                         "        order.id = index;",
                         "        order.answers = [];",
                         "        for (let index1 = 0; index1 < data[index].answers.length; index1++)",
                         "          order.answers.push(index1);",
                         "        for (var i = order.answers.length - 1; i > 0; i--) {",
                         "          var j = Math.floor(Math.random() * (i + 1));",
                         "          var temp = order.answers[i];",
                         "          order.answers[i] = order.answers[j];",
                         "          order.answers[j] = temp;",
                         "        }",
                         "        orders.push(order);",
                         "      }",
                         "      for (var i = orders.length - 1; i > 0; i--) {",
                         "        var j = Math.floor(Math.random() * (i + 1));",
                         "        var temp = orders[i];",
                         "        orders[i] = orders[j];",
                         "        orders[j] = temp;",
                         "      }",
                         "    }",
                         "    $('#stage-1').removeClass('show').addClass('hide');",
                         "    $('#stage-2').removeClass('hide').addClass('show');",
                         "    let number_html = $('#stage-2-number').html() + $('#problems').val();",
                         "    $('#stage-2-number').html(number_html);",
                         "    let score_html = 'Score:&nbsp;&nbsp;' + score + '/' + String(Number(problemNo)-1);",
                         "    $('#stage-2-score').html(score_html);",
                         "    let question_html = data[orders[0].id].problem;",
                         "    $('#stage-2-question').html('Question ' + problemNo + ':&nbsp;&nbsp;' + question_html);",
                         "    let answer_html = '<form id=\"form-' + problemNo + '\">';",
                         "    for (var k = 0; k <= data[orders[0].id].answers.length - 1; k++) {",
                         "      let answer_str =",
                         "        data[orders[0].id].answers[orders[problemNo - 1].answers[k]];",
                         "      if (",
                         "        data[orders[0].id].answers[orders[problemNo - 1].answers[k]].slice(",
                         "          0,",
                         "          1",
                         "        ) == '^'",
                         "      ) {",
                         "        answer_str = data[orders[0].id].answers[",
                         "          orders[problemNo - 1].answers[k]",
                         "        ].slice(1, -1);",
                         "      }",
                         "      if (data[orders[0].id].type == 0) {",
                         "        answer_html =",
                         "          answer_html +",
                         "          '<div style=\"margin-left:9%;margin-right:9%;display:flex;align-items:baseline;\"><input type=\"radio\" id=\"radio-' +",
                         "          problemNo +",
                         "          '-' +",
                         "          k +",
                         "          '\" name=\"radio-' +",
                         "          problemNo +",
                         "          '\"/><label class=\"pop1\" for=\"radio-' +",
                         "          problemNo +",
                         "          '-' +",
                         "          k +",
                         "          '\" id=\"label-' +",
                         "          k +",
                         "          '\">' +",
                         "          answer_str +",
                         "          '</label><br/></div>';",
                         "      } else {",
                         "        answer_html =",
                         "          answer_html +",
                         "          '<div style=\"margin-left:9%;margin-right:9%;display:flex;align-items:baseline;\"><input type=\"checkbox\" id=\"checkbox-' +",
                         "          problemNo +",
                         "          '-' +",
                         "          k +",
                         "          '\"/><label class=\"pop1\" for=\"checkbox-' +",
                         "          problemNo +",
                         "          '-' +",
                         "          k +",
                         "          '\" id=\"label-' +",
                         "          k +",
                         "          '\">' +",
                         "          answer_str +",
                         "          '</label><br/></div>';",
                         "      }",
                         "    }",
                         "    answer_html = answer_html + '<form/>';",
                         "    $('#stage-2-answer-div').html(answer_html);",
                         "  } ",
                         "  else {",
                         "    if (!testMethod) {",
                         "      $('#one').parent().addClass('invalid');",
                         "    }",
                         "    if ($('#problems').val() > data.length) {",
                         "      $('#problems').addClass('invalid');",
                         "    }",
                         "    if (!$('#player').val()) {",
                         "      $('#player').addClass('invalid');",
                         "    }",
                         "  }",
                         "}",
                         "function toNext() {",
                         "  if (flag == 0) {",
                         "    flag = 1;",
                         "    let check = true;",
                         "    let prevStr = '';",
                         "    let addStr = '';",
                         "    for (",
                         "      var k = 0;",
                         "      k <= data[orders[problemNo - 1].id].answers.length - 1;",
                         "      k++",
                         "    ) {",
                         "      if (",
                         "        data[orders[problemNo - 1].id].answers[",
                         "          orders[problemNo - 1].answers[k]",
                         "        ].slice(0, 1) == '^' &&",
                         "        document.getElementById('form-' + problemNo)[k].checked",
                         "      ) {",
                         "        prevStr = $('#label-' + k).html();",
                         "        addStr =",
                         "          '<img src=\"./assets/green.png\" style=\"width:20px;height:20px;\" alt=\"green\" />';",
                         "      } else if (",
                         "        data[orders[problemNo - 1].id].answers[",
                         "          orders[problemNo - 1].answers[k]",
                         "        ].slice(0, 1) == '^' &&",
                         "        document.getElementById('form-' + problemNo)[k].checked == false",
                         "      ) {",
                         "        prevStr = $('#label-' + k).html();",
                         "        addStr =",
                         "          '<img src=\"./assets/blue.png\" style=\"width:20px;height:20px;\" alt=\"blue\" />';",
                         "        check = false;",
                         "      } else if (",
                         "        data[orders[problemNo - 1].id].answers[",
                         "          orders[problemNo - 1].answers[k]",
                         "        ].slice(0, 1) != '^' &&",
                         "        document.getElementById('form-' + problemNo)[k].checked == false",
                         "      ) {",
                         "        prevStr = $('#label-' + k).html();",
                         "        addStr =",
                         "          '<img src=\"./assets/red.png\" style=\"width:20px;height:20px;\" alt=\"red\" />';",
                         "      } else {",
                         "        prevStr = $('#label-' + k).html();",
                         "        addStr =",
                         "          '<img src=\"./assets/red.png\" style=\"width:20px;height:20px;\" alt=\"red\" />';",
                         "        check = false;",
                         "      }",
                         "      $('#label-' + k).html(prevStr + '&nbsp;&nbsp;&nbsp;' + addStr);",
                         "    }",
                         "    if (check){ score++;",
                         "}",
                         " var score_str =  'Score:&nbsp;&nbsp;' + score + '/' + problemNo;",
                         "            $('#stage-2-score').html(score_str);",
                             "$('#btn-stage-2').html('NEXT');",
                         "  } ",
                         "  else {",
                         "    if (problemNo == $('#problems').val()) {",
                         "      $('#stage-2').removeClass('show');",
                         "      $('#stage-2').addClass('hide');",
                         "      $('#stage-3').removeClass('hide');",
                         "      $('#stage-3').removeClass('show');",
                         "      $('#myTitle').addClass('hide');",
                         "      var score_str = score + '/' + $('#problems').val();",
                         "            var additionalStr = Number(score)/Number($('#problems').val());additionalStr = Number(additionalStr)*100;$('#stage-3-score').html('Summary');            $('#stage-3-total-quiz').html('Number of Questions Generated For This Quiz: ' + $('#problems').val());",
                         "      $('#stage-3-quiz').html('Score For This Quiz: ' + score_str+'  (' + additionalStr.toFixed(1) + '%)');",
                         "      return;",
                         "    }",
                         "    problemNo++;",
                         "    flag = 0;",
                         "    let score_html = 'Score:&nbsp;&nbsp;' + score + '/' + String(Number(problemNo)-1);",
                         "    $('#stage-2-score').html(score_html);",
                         "    let question_html = data[orders[problemNo - 1].id].problem;",
                         "    $('#stage-2-question').html('Question ' + problemNo + ':&nbsp;&nbsp;' + question_html);",
                         "    let answer_html = '<form id=\"form-' + problemNo + '\">';",
                         "    for (",
                         "      var k = 0;",
                         "      k <= data[orders[problemNo - 1].id].answers.length - 1;",
                         "      k++",
                         "    ) {",
                         "      let answer_str =",
                         "        data[orders[problemNo - 1].id].answers[",
                         "          orders[problemNo - 1].answers[k]",
                         "        ];",
                         "      if (",
                         "        data[orders[problemNo - 1].id].answers[",
                         "          orders[problemNo - 1].answers[k]",
                         "        ].slice(0, 1) == '^'",
                         "      ) {",
                         "        answer_str = data[orders[problemNo - 1].id].answers[",
                         "          orders[problemNo - 1].answers[k]",
                         "        ].slice(1, -1);",
                         "      }",
                         "      if (data[orders[problemNo - 1].id].type == 0) {",
                         "        answer_html =",
                         "          answer_html +",
                         "          '<div style=\"margin-left:9%;margin-right:9%;display:flex;align-items:baseline;\"><input type=\"radio\" id=\"radio-' +",
                         "          problemNo +",
                         "          '-' +",
                         "          k +",
                         "          '\"  name=\"radio-' +",
                         "          problemNo +",
                         "          '\"/><label class=\"pop1\" for=\"radio-' +",
                         "          problemNo +",
                         "          '-' +",
                         "          k +",
                         "          '\" id=\"label-' +",
                         "          k +",
                         "          '\">' +",
                         "          answer_str +",
                         "          '</label><br/></div>';",
                         "      } else {",
                         "        answer_html =",
                         "          answer_html +",
                         "          '<div style=\"margin-left:9%;margin-right:9%;display:flex;align-items:baseline;\"><input type=\"checkbox\" id=\"checkbox-' +",
                         "          problemNo +",
                         "          '-' +",
                         "          k +",
                         "          '\" /><label class=\"pop1\" for=\"checkbox-' +",
                         "          problemNo +",
                         "          '-' +",
                         "          k +",
                         "          '\" id=\"label-' +",
                         "          k +",
                         "          '\">' +",
                         "          answer_str +",
                         "          '</label><br/></div>';",
                         "      }",
                         "    }",
                         "    answer_html = answer_html + '<form/>';",
                         "    $('#stage-2-answer-div').html(answer_html);",
                         "    $('#btn-stage-2').html('SUBMIT');",
                         "  }",
                         "}",
                         "function toStage4() {",
                         "  $('#stage-3').removeClass('show').addClass('hide');",
                         "  $('#stage-4').removeClass('hide').addClass('show');",
                         "  var score_str = score + '/' + $('#problems').val();",
                         "var additionalStr = Number(score)*100/Number($('#problems').val());$('#stage-4-score').html('Had obtained a score of ' + score_str + '  (' + additionalStr.toFixed(1) + '%)');",
                         "  $('#stage-4-score1').html('Had obtained a score of ' + score_str + '  (' + additionalStr.toFixed(1) + '%)');",
                         "  var name = $('#player').val();",
                         "  $('#stage-4-name').html(name);",
                         "  $('#stage-4-name1').html(name);",
                         "  var days = [",
                         "    'January',",
                         "    'Feburary',",
                         "    'March',",
                         "    'April',",
                         "    'May',",
                         "    'June',",
                         "    'July',",
                         "    'August',",
                         "    'September',",
                         "    'October',",
                         "    'November',",
                         "    'December',",
                         "  ];",
                         "  var myDate = new Date();",
                         "  $('#stage-4-date').html(",
                         "    myDate.getDate() +",
                         "      ' ' +",
                         "      days[myDate.getMonth()] +",
                         "      ' ' +",
                         "      myDate.getFullYear()",
                         "  );",
                         "  $('#stage-4-date1').html(",
                         "    myDate.getDate() +",
                         "      ' ' +",
                         "      days[myDate.getMonth()] +",
                         "      ' ' +",
                         "      myDate.getFullYear()",
                         "  );",
                         "}",
                         "function refresh() {",
                         "  window.location.replace('http://www.ianyhchua.com/md-1/biochem/menu.html')",
                         "}",
                         "async function toPDF() {",
                         "    var data = document.getElementById('certification1').innerHTML;",
                         "    myWindow = window.open('', '', 'width=600,height=800');",
                         "    myWindow.innerWidth = screen.width;",
                         "    myWindow.innerHeight = screen.height;",
                         "    myWindow.screenX = 0;",
                         "    myWindow.screenY = 0; ",
                         "    await myWindow.document.write(data);",
                         "    myWindow.focus();",
                         "    setTimeout(()=>{myWindow.print();myWindow.close();}, 500);",
                         "}",
                         "async function printpage() {",
                         "  var data = document.getElementById('certification1').innerHTML;",
                         "  myWindow = window.open('', '', 'width=600,height=800');",
                         "  myWindow.innerWidth = screen.width;",
                         "  myWindow.innerHeight = screen.height;",
                         "  myWindow.screenX = 0;",
                         "  myWindow.screenY = 0;",
                         "  await myWindow.document.write(data);",
                         "  myWindow.focus();",
                         "  setTimeout(()=>{myWindow.print();myWindow.close();}, 500);",
                         "}"]))
f1.writelines("\n".join([
    "<!DOCTYPE html>",
    "<head>",
    "<title>Page Title</title>",
    "<style>",
    "    body{",
    "        background-color: rgba(16,16,16,0.8);",
    "        color: white;",
    "    }",
    "    .title{",
    "        text-align:center;",
    "        font-family: system-ui,sans-serif;",
    "        border-width: 2px;",
    "        border-style: solid;",
    "        border-color: DodgerBlue !important;",
    "    }",
    "    .title1{",
    "    text-align:center;",
    "    text-transform: uppercase;",
    "    font-family: verdana;",
    "    font-size: 2em;",
    "    font-weight: 700;",
    "    color: rgba(224, 255, 255, 0.8);",
    "    text-shadow: 1px 1px 1px #919191,",
    "        1px 2px 1px #919191,",
    "        1px 3px 1px #919191,",
    "        1px 4px 1px #919191,",
    "        1px 5px 1px #919191,",
    "        1px 6px 1px #919191,",
    "        1px 7px 1px #919191,",
    "        1px 8px 1px #919191,",
    "        1px 9px 1px #919191,",
    "        1px 10px 1px #919191,",
    "        1px 18px 6px rgba(16,16,16,0.4),",
    "        1px 22px 10px rgba(16,16,16,0.2),",
    "        1px 25px 35px rgba(16,16,16,0.2),",
    "        1px 30px 60px rgba(16,16,16,0.4);",
    "}",
    "    .title2{",
    "    text-align: center;",
    "    text-transform: uppercase;",
    "    font-family: verdana;",
    "    font-size: 1em;",
    "    font-weight: 700;",
    "    color: rgba(173, 216, 230, 0.8);",
    "    text-shadow: ",
    "        1px 1px 1px #919191,",
    "        1px 2px 1px #919191,",
    "        1px 3px 1px #919191,",
    "        1px 4px 1px #919191,",
    "        1px 5px 1px #919191,        ",
    "        1px 10px 6px rgba(16,16,16,0.4),",
    "        1px 13px 10px rgba(16,16,16,0.2),",
    "        1px 15px 35px rgba(16,16,16,0.2),",
    "        1px 6px 15px rgba(16,16,16,0.4);",
    "    }",
    "    .container{",
    "        margin-top:20px;",
    "        text-align: center;",
    "    }",
    "    .board-header{",
    "        margin: 10px 5px 10px 5px;",
    "        min-height: 30px;",
    "    }",
    "    .board-body{",
    "        margin: 20px 5px 20px 5px;        ",
    "        min-height: 200px;",
    "        color:#e7e4e4;",
    "    }",
    "    .board-body-footer{",
    "        margin: 20px 5px 10px 5px;        ",
    "        min-height: 50px;",
    "    }",
    "    .intend{",
    "        text-align: left;",
    "        text-indent: 25%;",
    "    }",
    "    .form-group {",
    "        text-align: left;",
    "    }",
    "    .form-group p{",
    "        display: inline;",
    "    }",
    "    input{",
    "        height:40px;",
    "        border-color: DodgerBlue !important;",
    "        border-style: solid;",
    "        border-width: 1px;",
    "    }",
    "    .preference-div{",
    "        display: flex;",
    "        justify-content: center;",
    "        align-items: center;",
    "        flex-direction: column;",
    "    }",
    "    .pref-list{",
    "        width:50%;",
    "        margin:10px;",
    "        text-align: left;",
    "        min-height: 80px;",
    "        color:rgb(14, 2, 2);",
    "        background-color: rgba(224, 255, 255, 0.8);",
    "        font-size: 20px;",
    "    }",
    "    .pref-list>ul>li{",
    "        font-size: 20px;",
    "    }",
    "    label{",
    "        font-size: 20px;",
    "    }",
    "    .hide{",
    "        display: none;",
    "    }",
    "    p {",
    "        font-size:20px;",
    "    }",
    "    .btn{",
    "        padding: 10px 20px;",
    "        border:1px solid green !important;",
    "        border-radius: 10px;",
    "        transition: all 0.2s ease-in-out;",
    "    }",
    "   .btn-primary{",
    "        background-color: white;",
    "        color: green;",
    "        font-size: 25px;",
    "    }",
    "    .btn-large{",
    "        padding: 10px 30px;",
    "        background-color: white;",
    "        color: green;",
    "        font-size:25px;",
    "        margin-right: 20px;",
    "    }",
    "    .btn-primary:hover{",
    "        background-color: green;",
    "        padding: 10px 30px;",
    "        color:white;",
    "    }",
    "    .btn-large:hover{",
    "        background-color: green;",
    "        color:white;",
    "    }",
    "    .score-div{",
    "        display: flex;",
    "        justify-content: space-between;",
    "    }",
    "    .animate-font{",
    "        font-size:40px;",
    "        color:aqua;",
    "        margin-top:0px;",
    "        margin-bottom:0px;",
    "    }",
    "    input[type=radio]{",
    "        height:15px;",
    "        margin-top:10px;",
    "        margin-bottom:10px;",
    "    }",
    "    input[type=checkbox]{",
    "        height:15px;",
    "        margin-top:10px;",
    "        margin-bottom:10px;",
    "    }",
    "    .question-div, .answer-div{",
    "        text-align: left;",
    "        margin-bottom:20px;",
    "    }",
    "    .question-div p{",
    "        margin: 5px 5px 5px 5px;",
    "    }",
    "    #stage-3-score{",
    "        text-align: center;",
    "    }",
    "    .achievement-div{",
    "        margin-top:30px;",
    "        text-align: center;",
    "        border: 1px solid lightgrey !important;",
    "        margin-bottom:20px;        ",
    "    }",
    "    .achievement-div p{",
    "        font-size: 30px;",
    "    }",
    "    .certificate-btn-div{",
    "        position:absolute;",
    "        right:3%;",
    "        top:40px;",
    "    }",
    "    .btn-absolute{",
    "        width:250px;",
    "        margin:10px;",
    "    }",
    "    .certificate-div{",
    "        width:50%;",
    "        min-height:900px;",
    "        margin-top:10px;",
    "        margin-bottom:10px;",
    "        border: 2px solid DodgerBlue;",
    "        position:relative;",
    "        display: flex;",
    "        align-items: center;",
    "        flex-direction: column;",
    "    }",
    "    h2{",
    "        margin-top:40px;",
    "    }",
    "    .certificate-div>.bottom{",
    "        position: absolute;",
    "        bottom:30px;",
    "    }",
    "    .certificate-div h4, .certificate-div p, .certificate-div img{",
    "        text-align: center;",
    "        margin:5px;",
    "    }",
    "    div.bottom div p{",
    "        margin:5px !important;",
    "    }",
    "    .certificate-div h4{",
    "        color:DodgerBlue;",
    "    }",
    "    .certificate-panel{",
    "        display:flex;",
    "        justify-content: center;",
    "        background-color: white;",
    "        color: black;    ",
    "    }",
    "    p.bold_p{",
    "        color:blue;",
    "    }",
    "    .invalid{",
    "        border-width:1px !important;",
    "        border-style: solid !important;",
    "        border-color:red !important;",
    "    }",
    "    .true{",
    "        color:red;",
    "    }",
    "    label.pop{",
    "        position: relative;",
    "    }",
    "    label.pop1{",
    "        position: relative;",
    "    }",
    "    label.pop:hover{",
    "        left: -1px;",
    "        top: -1px;",
    "        color:rgb(134, 15, 15);",
    "    }",
    "    label.pop1:hover{",
    "        left: -1px;",
    "        top: -1px;",
    "        color:#04AA6D;",
    "    }   #stage-4-name{font-style: italic;}",
    "</style>",
    "</head>",
    "<body>",
    "    <div class='title' id='myTitle'>",
    "        <div class='title1'>",
    "            <h1 style='margin-top:20px; margin-bottom: 20px'>"+title+"</h1>",
    "        </div>",
    "        <div class='title2'>",
    "            <h2>"+sub_title+"</h2>",
    "        </div>",
    "    </div>",
    "    <div class='container'>",
    "        <div class='board-body'>",
    "            <div class='show' id='stage-1'>",
    "                <form>",
    "                    <p>Quiz Setup</p>",
    "                    <div class='intend'>",
    "                        <div class='form-group'>",
    "                            <p>Total Number of Questions Available: </p>",
    "                            <label id='numbers'></label>",
    "                        </div>",
    "                        <div class='form-group'>",
    "                            <p>Number of Questions To Be Generated For This Quiz:</p>",
    "                            <input type='number' id='problems' placeholder='30' min='1' max='50' value='1'/>",
    "                        </div>",
    "                    </div>",
    "                    <div class='preference-div'>",
    "                        <div class='pref-list'>",
    "                            <p>&nbsp;&nbsp;Quiz Preference:</p>",
    "                            <input type='radio' id='one' name='my_radio' value='one' >",
    "                            <label class='pop' for='one'>No randomization of questions or answer options</label><br>",
    "                            <input type='radio' id='two' name='my_radio' value='two'>",
    "                            <label class='pop' for='two'>Randomize order of questions only</label><br>",
    "                            <input type='radio' id='three' name='my_radio' value='three'>",
    "                            <label class='pop' for='three'>Randomize order of both questions and answer options</label>",
    "                        </div>",
    "                    </div>",
    "                    <div class='intend'>",
    "                        <div class='form-group'>",
    "                            <label>Student Name:</label>",
    "                            <input type='text' id='player' placeholder='Romeo de Juliet' value=''/>",
    "                        </div>",
    "                    </div>",
    "                    <div class='board-body-footer'>",
    "                        <button class='btn btn-primary' type='button' id='btn-stage-1' onclick='goTwoStage()'>START</button>",
    "                    </div>",
    "                </form>",
    "            </div>",
    "            <div class='hide' id='stage-2'>",
    "                    <div class='score-div'>",
    "                        <p id='stage-2-number'>Number of Questions Generated For This Quiz: </p>",
    "                        <p id='stage-2-score' class='animate-font'>score:</p>",
    "                    </div>",
    " <div style='border:1px #e7e4e4 solid'>",
    "                    <div class='question-div'>",
    "                        <p class='stage-2-question' id='stage-2-question' style='margin-left: 20px !important;'></p>",
    "                    </div>",
    "                    <div class='answer-div' id='stage-2-answer-div'>",
    "                        <input type='checkbox'/><label>ans1</label><br/>",
    "                        <input type='checkbox'/><label>ans2</label><br/>",
    "                        <input type='checkbox'/><label>ans3</label><br/>",
    "                    </div>",
    "                    </div>",
    "                    <div class='board-body-footer'>",
    "                        <button class='btn btn-primary' type='button' id='btn-stage-2'  onclick='toNext()'>SUBMIT</button>",
    "                    </div>",
    "            </div>",
    "            <div class='hide' id='stage-3'>",
    "                <div class='score-div1'>",
    "                    <p></p>",
    "                    <p class='animate-font' id='stage-3-score'>score:0/0</p>",
    "                </div>",
    "                <div class='achievement-div'>",
    "                    <p id='stage-3-total-quiz'>Number of Questions Generated For This Quiz: 30</p>",
    "                    <p id='stage-3-quiz'>Score For This Quiz: 1/3</p>",
    "                    <p>End of Quiz</p>",
    "                </div>",
    "                <div class='board-body-footer'>",
    "                    <button class='btn btn-large' type='button' onclick='toStage4()'>Print Certificate of Achievement",
    "                    </button>",
    "                    <button class='btn btn-large' type='button' onclick='refresh()'>Back to Main Menu",
    "                    </button>",
    "                </div>",
    "            </div>",
    "            <div class='hide' id='stage-4'>",
    "                <div class='certificate-btn-div'>",
    "                    <button class='btn btn-large btn-absolute' onclick='printpage()' >Print Hard Copy</button><br/>",
                        "<button class='btn btn-large' style='margin-right: 0px; font-size: 22px' type='button' onclick='refresh()'>Back to Main Menu</button>",
    "                </div>",
    "                <div class='certificate-panel' id='certification'>",
    "                    <div class='certificate-div' >",
    "                        <h2>CERTIFICATE of ACHIEVEMENT</h2>",
    "                        <img src='./assets/mark.png' alt='mark' style='width:25%'/>",
    "<br/><br/><br/><br/><br/><p>This certifies that</p>",
    "                        <p id='stage-4-name'></p>",
    "                        <p id='stage-4-score'></p>",
    "                        <p>Upon completing the quiz on</p>",
    "                        <p id='stage-4-date'>3 January 2023</p>",
    "                        <p>For</p>",
    "                        <p class='bold_p'>"+title+"</p>",
    "                        <p class='bold_p'>"+sub_title+"</p>",
    "                        <div class='bottom'>",
    "                            <div style='text-align: center;'>",
    "                                <p >No signature is required for this certificate</p>",
    "                                <p >Generated by i-Med Learning Systems</p>",
    "                            </div>",
    "                        </div>",
    "                    </div>",
    "                </div>",
    "            </div>",
    "        </div>",
    "    </div>",
    "    <div  id='certification1' style='display:none;background-color: white; color: black; border: solid 1px dodgerblue; width: 600px; height: 1000px;'>",
    "        <div style='display: flex; align-items: center; flex-direction: column;'>",
    "            <h2>CERTIFICATE of ACHIEVEMENT</h2>",
    "            <img  style='margin-top: 100px;' src='./assets/mark.png' alt='mark' style='width:25%'/>",
    "<br/><br/><br/><br/><br/>",
    "            <p style='margin:5px;'>This certifies that</p>",
    "            <p style='margin:5px;font-style:italic' id='stage-4-name1'></p>",
    "            <p style='margin:5px;' id='stage-4-score1'></p>",
    "            <p style='margin:5px;'>Upon completing the quiz on</p>",
    "            <p style='margin:5px;' id='stage-4-date1'>3 January 2023</p>",
    "            <p style='margin:5px;'>For</p>",
    "            <p style='margin:5px;color:blue;' class='bold_p'>"+title+"</p>",
    "            <p style='margin:5px;color:blue;' class='bold_p'>"+sub_title+"</p>",
    "            <div class='bottom' style='margin-top: 200px;'>",
    "                <div style='text-align: center;'>",
    "                    <p >No signature is required for this certificate</p>",
    "                    <p >Generated by i-Med Learning Systems</p>",
    "                </div>",
    "            </div>",
    "        </div>",
    "    </div>",
    "</body>",
    "<script src='./assets/jquery.min.js'></script>",
    "<script src='"+file_name+".js'></script>",
    "</html>"

]))
f.close()
f1.close()
f2.close()