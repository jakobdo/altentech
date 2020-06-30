import React from 'react';

import { Icon } from 'react-materialize';

interface StarsProps {
    level: number;
}

function Stars({level}:StarsProps){
    let stars = [];

    // Full stars
    for(let x: number = 1; x <= level; x++){
        stars.push(<Icon key={`full_${x}`}>star</Icon>)
    }

    // Empty stars
    for(let x: number = 1; x <= 5-level; x++){
        stars.push(<Icon key={`empty_${x}`}>star_border</Icon>)
    }

    return (
        <React.Fragment>
            {stars}
        </React.Fragment>
    )
}

export default Stars;