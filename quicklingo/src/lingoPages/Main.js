
import './App.css';
import {useHistory, useLocation} from 'react-router-dom'
import React from 'react';

function Main() {
  let history = useHistory();
  const location = useLocation();
  console.log(location.pathname)
  return (
    <div className="App">
      <h1 className='neon' data_text='Welcome to QuickLingo'>Welcome to QuickLingo</h1>
        
        <h2 className='neon2' data_text='Please Select a catagory' >Please Select a catagory</h2>

          <a id='chinese' onClick={() => {history.push('/chinese')}} className="neon-button">Chinese</a>
          <a id='french' href='#wewe' className="neon-button">French</a>

    </div>
  );
}

export default Main;
