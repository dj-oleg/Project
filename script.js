function CheckAnswer(){
    var answers = document.getElementsByName("answer")
    var counter = 1
    var myansw = document.getElementById("answ").innerHTML
    var answer_user = 0
    var answer1 = 0 
    for (item1 of answers){
        console.log(item1)
        if (item1.checked==true){
            answer1++
        }
    }
    if (answer1==0){
        alert("Немає відповіді")
    }
    else{      
    for (items of answers){
        if (items.checked==true){
            console.log("Обрали варіант:"+counter)
            if(counter==Number(myansw)){
                alert("Вірно")
                answer_user = "y"

                
            }
            else{
                alert("Невірно")
                answer_user = "n"
            }
            

        }
        counter++
    }

var xhr = new XMLHttpRequest();
var testnumber = 1
xhr.open('GET', '/saveanswers?test='+testnumber+'&answ='+answer_user, false);

// 3. Отсылаем запрос
xhr.send();

// 4. Если код ответа сервера не 200, то это ошибка
if (xhr.status != 200) {
  // обработать ошибку
//   alert( xhr.status + ': ' + xhr.statusText ); // пример вывода: 404: Not Found
} else {
    var next_link = document.getElementById("answ").nextElementSibling.href
    Location.href=next_link
}
}
}
