import React, { useState, useEffect } from 'react';

import API from '../utils/API';
import { Card, Row } from 'react-materialize';
import { useParams } from 'react-router-dom';
import Loading from '../common/Loading';
import { ITechnology } from '../models/Technology';
import ConsultantLink from '../common/ConsultantLink';
import { IConsultantSimple } from '../models/Consultant';

function TechnologyDetail(){
    const { technologySlug } = useParams();
    const [technology, setTechnology] = useState<ITechnology | null>(null);

    useEffect(() => {
        const fetchTechnology = async() => {
            const result = await API.get(`/technologies/${technologySlug}/`);
            setTechnology(result.data);
        };
        fetchTechnology();
    }, [technologySlug]);

    return (
        <div className="container">
            {technology ? (
                <React.Fragment>
                    <h1>{technology.name}</h1>
                    <Card>
                        {technology.description}
                    </Card>
                    {technology.consultants.length > 0 && (
                        <React.Fragment>
                            <h2>Consultants</h2>
                            <Row>
                                {technology.consultants.map((consultant: IConsultantSimple) => (
                                    <ConsultantLink key={consultant.slug} consultant={consultant} />
                                ))}
                            </Row>
                        </React.Fragment>
                    )}
                </React.Fragment>
            ) : (
                <Loading />
            )}
            
        </div>
    )
}

export default TechnologyDetail;
