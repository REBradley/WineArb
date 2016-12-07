import React from 'react';

const Image = (props) => {
    return(
        <img className="Image"
            src={props.url}
            alt='Responsive Image'
        />
    );
}

export { Image };