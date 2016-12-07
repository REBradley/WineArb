import React from 'react';
import ReactDOM from 'react-dom';

const Title = (props) => {
    return (
        <div className="TitleGroup">
            <h2 className="main_title_text">{props.main_title}</h2>
            <h3 className="sub_title_text">{props.sub_title}</h3>
        </div>
    );
};

export default Title;
