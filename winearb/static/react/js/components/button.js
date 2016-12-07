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

export default LinkButton;
