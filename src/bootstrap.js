//  We are building a casino!
//  You are to build one casino game, black jack, slots, roulette, etc, ( these are the ones I have seen built out before.)

//  Requirements:
//  -Build the game.
//  -The player will have a wallet, they can add money to the wallet, any winnings they get will be added to the wallet.
//  -If the wallet goes empty they must add more money or they have to stop playing.
//  -They need to be able to stop playing and cash out the wallet at anytime. (bonus if the cash out proccess tells them if they made a profit or not)
//  -let the player set the dollar/cents amount of the bet (in the game).
//  -let them continue playing as long as they have money or decide to cash out.

//  -Make a git repository for the project.
//  -Push a new commit up to github each day.

const wallet = 1000;

function greeting() {
    console.log("Hello, welcome to Mos Eisley Cantina! This is Star Wars Slots");
    console.log("You have" + " " + wallet + " " + "credits in your wallet");
}

greeting();
const bet = 0;
bet.input = ("What is your bet? (10, 20, 50, 100)");

function placeBet() {
    return Number(bet);
}

const answer = console.log("Your bet is" + " " + bet + ". " + "You now have" + " " + (wallet - bet) + " " + "credits in your wallet")
    

placeBet(answer);

const weightedLottery = sabers => {
    let containerArray = [];

    Object.keys(sabers).forEach(key =>{
        for (let i = 0; i < sabers[key]; i++) {
            containerArray.push(key);
        }
    })

    return containerArray[(Math.random() * containerArray.length) | 0];
}

const sabers = {
    purpleSaber: 1,
    redSaber: 2,
    greenSaber: 4,
    empty: 10
}

const spinOutput = weightedLottery(sabers);

function slotOutput() {
    console.log("The slot rolls" + " " + spinOutput);
}

console.log(slotOutput());
console.log(slotOutput());
console.log(slotOutput());