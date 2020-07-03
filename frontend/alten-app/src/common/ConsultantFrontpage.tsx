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
                <Link to={`/consultants/${consultant.slug}`}>
                <img
                    className="circle responsive-img"
                    src={consultant.image.medium} 
                    alt={consultant.fullname} 
                    />
                </Link>
            </Col>
            <Col s={12} m={8}>
                <h3>
                    <Link to={`/consultants/${consultant.slug}`}>{consultant.fullname}</Link>
                </h3>
                <h6>{consultant.jobtitle}</h6>
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