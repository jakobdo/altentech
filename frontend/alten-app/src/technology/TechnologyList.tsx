import React, { useState, useEffect } from 'react';

import API from '../utils/API';
import { Row, Col } from 'react-materialize';
import { Link } from 'react-router-dom';
import { ITechnology } from '../models/Technology';

function TechnologyList(){
    const [technologies, setTechnologies] = useState<ITechnology[]>([]);

    useEffect(() => {
        const fetchTags = async() => {
            const result = await API.get('/technologies/');
            setTechnologies(result.data);
        };
        fetchTags();
    }, []);

    return (
        <div className="container">
            <h1>Technologies & Tools</h1>
            <Row>
                <div className="collection">
                    {technologies.map((technology: ITechnology) => 
                        <Col s={12} m={6} l={4} xl={3}>
                            <div className="card"
                            >
                                <Link 
                                    className="collection-item"
                                    to={`/technologies/${technology.slug}`}
                                >
                                    {technology.name}
                                </Link>
                            </div>
                        </Col>
                    )}
                </div>
            </Row>
        </div>
    )
}

export default TechnologyList;
