let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:
function generateTarget() {
  return Math.floor(Math.random() * 10));
}

const compareGuesses = (userGuess, computerGuess, secretNumber) => {
  userDiff = Math.abs(userGuess, secretNumber);
  computerDiff = Math.abs(computerGuess, secretNumber);
  
  if (userDiff === computerDiff) {
    return true;
  }
  else if(userDiff > computerDiff) {
    return false;
  }
  else {
    return true;
  }
  
}

function updateScore('') {
  if updateScore('human') {
    humanScore += 1;
  }
  else if updateScore('computer') {
    computerScore += 1;
  }
  else {
    console.log('Invalid winner!');
  }
}

function advanceRound() {
  currentRoundNumber ++;
}

generateTarget();
