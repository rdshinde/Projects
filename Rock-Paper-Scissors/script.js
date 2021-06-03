let userScore = 0;
let computerScore = 0;

const userScore_span = document.getElementById("user-score");
const computerScore_span = document.getElementById("computer-score");
const scoreBoard_div = document.querySelector(".score-board");
const result_div = document.querySelector(".result > p");
const rock_div = document.getElementById("r");
const paper_div = document.getElementById("p");
const scissors_div = document.getElementById("s");

function getComputerChoice(){
    const choices = ['r','p','s'];
    const randomNumber = Math.floor(Math.random() * 3);
    return choices[randomNumber];
}

function convertToWord(letter){
    if(letter === "r") return "Rock";
    if(letter === "p") return "Paper";
    return "Scissors"
}

function wins(userChoice,computerChoice){
    const user = "(User)".fontsize(3).sub(); 
    const comp = "(Computer)".fontsize(3).sub(); 
    userScore++;
    userScore_span.innerHTML = userScore;
    computerScore_span.innerHTML = computerScore;
    result_div.innerHTML = convertToWord(userChoice )+user + " beats " + convertToWord(computerChoice)+comp +" . You win. 🔥 🔥 🔥 "
    document.getElementById(userChoice).classList.add('green-glow');
    setTimeout(function(){document.getElementById(userChoice).classList.remove('green-glow')},1500);

    document.getElementById("scores").classList.add('green-bg');
    setTimeout(function(){document.getElementById("scores").classList.remove('green-bg')},1500);

}


function lose(userChoice,computerChoice){
    computerScore++;
    const user = "(User)".fontsize(3).sub(); 
    const comp = "(Computer)".fontsize(3).sub();  
    userScore_span.innerHTML = userScore;
    computerScore_span.innerHTML = computerScore;
    result_div.innerHTML = convertToWord(computerChoice )+comp + " beats " + convertToWord(userChoice)+user +" . You lose. 👎🏻 👎🏻 👎🏻 "

    document.getElementById(userChoice).classList.add('red-glow');
    setTimeout(function(){document.getElementById(userChoice).classList.remove('red-glow')},1500);

    document.getElementById("scores").classList.add('red-bg');
    setTimeout(function(){document.getElementById("scores").classList.remove('red-bg')},1500);
}


function draw(userChoice,computerChoice ){
    const user = "(User)".fontsize(3).sub(); 
    const comp = "(Computer)".fontsize(3).sub();  
    result_div.innerHTML = convertToWord(computerChoice )+comp + " equals " + convertToWord(userChoice)+user +" . Game Draw .🤜🏻🤛🏻 🤜🏻🤛🏻 🤜🏻🤛🏻 "

    document.getElementById(userChoice).classList.add('grey-glow');
    setTimeout(function(){document.getElementById(userChoice).classList.remove('grey-glow')},1500);

    document.getElementById("scores").classList.add('grey-bg');
    setTimeout(function(){document.getElementById("scores").classList.remove('grey-bg')},1500);
    
}


function game(userChoice){
    const computerChoice = getComputerChoice();
    switch(userChoice + computerChoice){
        case "rs":
        case "pr":
        case "sp":
            wins(userChoice,computerChoice);
            break;
        case "rp":
        case "ps":
        case "sr":
            lose(userChoice,computerChoice);
            break;
        case "rr":
        case "pp":
        case "ss":
            draw(userChoice,computerChoice);
            break;

    }
}


function main(){
    rock_div.addEventListener('click',function(){
        // console.log("rock");
        game("r");
    })
    
    paper_div.addEventListener('click',function(){
        // console.log("paper");
        game("p");
    })
    
    scissors_div.addEventListener('click',function(){
        // console.log("scissors");
        game("s");
    })
}

main();