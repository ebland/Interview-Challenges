	const wordlist = ['APPLE', 'PLEAS', 'PLEASE'];
	const puzzles= ['AELWXYZ', 'AELPXYZ', 'AELPSXY', 'SAELPXY', 'XAELPSY'];
	//output: [0, 1, 3, 2, 0]


function spellingBeeSolutions(wordlist, puzzles) {
    let newArr = [];

    for (let i = 0; i < puzzles.length; i++) {
        newArr.push(0);
    }

    for (let i = 0; i < puzzles.length; i++) {
        for (let j = 0; j < wordlist.length; j++) {
            if (checkWordList(puzzles[i], wordlist[j])) {
                newArr[i]++;
            }
        }  
    }
    return newArr;
}

const checkWordList = (wordlist1, wordlist2) => {
    let wordlistObj = {};
    let inside = true;
    let count = 0;
    

    for (let i = 0; i < wordlist2.length; i++) {
        if (wordlistObj[wordlist2[i]]) {
            wordlistObj[wordlist2[i]]++;
        } else {
            wordlistObj[wordlist2[i]] = 1;
        }
    }

    for (let i = 0; i < wordlist2.length; i++) {
        if (!wordlist2.includes(wordlist1[i])) {
            return false;
        }

        if (wordlist1.includes(wordlist2[i])) {
               for (key in wordlistObj) {
                    if (key === wordlist2[i]) {
                        count += wordlistObj[key];
                    }
               }
               if (count === wordlist2.length) {
                    return inside;
               }
            } else {
                inside = false;
                break;
            }
        }
    
    return inside;

}
	
console.log(spellingBeeSolutions(wordlist, puzzles))
