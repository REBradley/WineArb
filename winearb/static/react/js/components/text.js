import React from 'react';
import ReactDOM from 'react-dom';

const Text = (props) => {
    return (
        <div className="Text">
            <p className="main_text">{props.text}</p>
        </div>
    );
};

export default Text;
