import React from 'react';

import { Row, Col } from 'react-materialize';

import { IConsultant } from '../models/Consultant';
import { Link } from 'react-router-dom';
import TechnologyLevels from './TechnologyLevels';

interface ConsultantFrontpageProps {
    consultant: IConsultant
}

function ConsultantFrontpage({consultant}:ConsultantFrontpageProps){
    return (
        <Row>
            <Col s={12} m={4}>
                <img
                    className="circle responsive-img"
                    src={consultant.image.medium} 
                    alt={consultant.fullname} 
                />
            </Col>
            <Col s={12} m={8}>
                <h3>
                    <Link to={`/consultants/${consultant.slug}`}>{consultant.fullname}</Link>
                </h3>
                <h5>{consultant.jobtitle}</h5>
                <p>{consultant.teaser}</p>
                <TechnologyLevels technologyLevels={consultant.technologyLevels} />
            </Col>
            <Col s={12} className="center-align">
                <Link className="waves-effect waves-light btn" to={`/consultants/${consultant.slug}`}>LEARN MORE</Link>
            </Col>
        </Row>
    )
}

export default ConsultantFrontpage;