import React, { useState, useEffect } from 'react';

import { IConsultant } from '../models/Consultant';
import API from '../utils/API';
import { Row, Col, Chip, Card } from 'react-materialize';
import { ITag } from '../models/Tag';
import { Link, useParams } from 'react-router-dom';

function ConsultantList(){
    const { tagSlug } = useParams();
    const [consultants, setConsultants] = useState<IConsultant[]>([]);
    const [tags, setTags] = useState<ITag[]>([]);

    useEffect(() => {
        const fetchConsultants = async() => {
            let url = '/consultants/';
            if(tagSlug){
                url = `/consultants/tags/${tagSlug}/`
            }
            const result = await API.get(url);
            setConsultants(result.data);
        };
        fetchConsultants();
    }, [tagSlug]);

    useEffect(() => {
        const fetchTags = async() => {
            const result = await API.get('/tags/');
            setTags(result.data);
        };
        fetchTags();
    }, []);

    return (
        <div className="container">
            <h1>Consultants</h1>
            <div>
                <Link to="/consultants">
                    <Chip close={false}>All</Chip>
                </Link>
                {tags.map((tag: ITag) => 
                    <Link to={`/consultants/tags/${tag.slug}`}>
                        <Chip close={false}>{tag.name}</Chip>
                    </Link>
                )}
            </div>
            <hr />
            <Row>
                {consultants.map((consultant: IConsultant) => 
                    <Col s={12} m={6} l={4}>
                        <Card
                            actions={[
                                <Link 
                                    to={`/consultants/${consultant.slug}`}
                                    className="waves-effect waves-light btn"
                                >LEARN MORE</Link>
                            ]}
                            textClassName="center-align"
                        >
                            <Link 
                                to={`/consultants/${consultant.slug}`}
                            >
                                <img 
                                    className="circle responsive-img"
                                    src={consultant.image.medium} 
                                    alt={consultant.fullname} 
                                />
                            </Link>
                            <strong>{consultant.fullname}</strong>
                            <p>{consultant.jobtitle}</p>
                        </Card>
                    </Col>
                )}
            </Row>
        </div>
    )
}

export default ConsultantList;
