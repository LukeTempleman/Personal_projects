
import React, {useState, useEffect} from 'react';
import './App.css';


let arr = ['Mouth','Fire','Person','Tree','Mountain','Sun', 'Moon','Door','Woman','Roof','King','Water']
let arr2 = ['Follow','Crowd','Big','Dog','Too Much','Everyone','Adult','Public','Wife','Bark','Angry','Woods','Forest','Rest','Volcano','Argument','Adultery','Queen']
  
  


function Chinese(){
  const [count, setCount] = useState(5)
  const [word, setWord] = useState('')
  let finalWord = arr.sort(() => Math.random() - 0.5)
  
  let start = true
  
  useEffect(() =>{
    if (count > 0 && start === true){
      setTimeout(() => setCount(count - 1), 1000);
    }
    else{
      setCount("Start")
      start = false
      setCount(7)

      for (var i = 0; i < finalWord.length; i++) {
        if (count > 0){
          setTimeout(() => setCount(count - 1), 1000);
        }
          else{
            setWord(finalWord[i])
            
          }
        }


      }

  })
  


  return (
        <div>
          <a className='neon'>{count}</a>
          <h1 className='neon3'>{word}</h1>
          
        </div>
        );
    }
export default Chinese;
