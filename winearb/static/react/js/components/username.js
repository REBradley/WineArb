import React from 'react';

const Username = (props) => {
    return(
        <div className="UserName">
             <h5>by {props.username}</h5>
        </div>
    )
}

export { Username };