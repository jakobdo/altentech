import React from 'react';

import { Row, Col } from 'react-materialize';

import { Link } from 'react-router-dom';
import { ITechnologyLevel } from '../models/TechnologyLevel';
import Stars from './Stars';

interface TechnologyLevelsProps {
    technologyLevels: ITechnologyLevel[];
}

function TechnologyLevels({technologyLevels}:TechnologyLevelsProps){
    return (
        <Row>
            {technologyLevels.map((level: ITechnologyLevel) => 
                <React.Fragment key={level.id}>
                    <Col s={6} className="right-align">
                        <Link to={`/technologies/${level.slug}`}>{level.name}</Link>
                    </Col>
                    <Col s={6}><Stars level={level.level} /></Col>
                </React.Fragment>
            )}
        </Row>
    )
}

export default TechnologyLevels;