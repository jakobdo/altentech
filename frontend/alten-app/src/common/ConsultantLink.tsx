import React from 'react';

import { Col, Card } from "react-materialize";
import { Link } from "react-router-dom";
import { IConsultantSimple } from '../models/Consultant';

interface ConsultantLinkProps {
    consultant: IConsultantSimple
}

function ConsultantLink({consultant}:ConsultantLinkProps){
    return (
        <Col s={12} m={6} l={4}>
            <Card
                actions={[
                    <Link
                        key={`consult_key_${consultant.slug}`}
                        className="waves-effect waves-light btn" 
                        to={`/consultants/${consultant.slug}`}
                    >
                        Learn More
                    </Link>
                ]}
                textClassName="center-align"
            >
                <Link to={`/consultants/${consultant.slug}`}>
                    <img 
                        className="circle responsive-img"
                        src={consultant.image.medium} 
                        alt={consultant.fullname} 
                    />
                </Link>
                <h5>{consultant.fullname}</h5>
                <strong>{consultant.jobtitle}</strong>
            </Card>
        </Col>
    )
}

export default ConsultantLink;