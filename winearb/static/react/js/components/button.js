import React from 'react';

import Button from 'react-bootstrap/lib/Button';


const LinkButton = (props) => {
    return (
        <div className="LinkedButton">
            <Button href={props.link} className="btn" bsSize="xsmall" >
                {props.label}
            </Button>
        </div>
    );
}

const LinkButtonAdder = (Component, props) => {
    const Btn = LinkButton(props)
    return (
        <div className="ComponentWithLink">
            <div>
                <Component />
            </div>
            <div>
                { Btn }
            </div>
        </div>
    );
}

export default LinkButton;