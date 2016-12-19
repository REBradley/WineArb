import React from 'react';
import ReactDOM from 'react-dom';

const Text = (props) => {
    return (
        <div className="Text" style={{textAlign:'left'}}>
            <p className="main_text">{props.text}</p>
        </div>
    );
};

export default Text;
