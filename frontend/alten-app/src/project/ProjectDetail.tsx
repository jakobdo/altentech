import React, { useState, useEffect } from 'react';

import { IProject } from '../models/Project';
import API from '../utils/API';
import Loading from '../common/Loading';
import { useParams, Link } from 'react-router-dom';
import { Card, Row, Col } from 'react-materialize';
import { ITechnologySimple } from '../models/Technology';
import { IConsultantSimple } from '../models/Consultant';

function ProjectDetail(){
    const { projectSlug } = useParams();
    const [project, setProject] = useState<IProject | null>(null);

    useEffect(() => {
        const fetchData = async() => {
            const result = await API.get(`/projects/${projectSlug}/`);
            setProject(result.data);
        };
        fetchData();
    }, [projectSlug]);

    return (
        <div className="container">
            {project ? (
                <React.Fragment>
                    <h1>{project.name}</h1>
                    <Card>
                        <table className="highlight">
                            <tbody>
                                <tr>
                                    <th>Industry: </th>
                                    <td>{project.industry}</td>
                                </tr>
                                <tr>
                                    <th>Description: </th>
                                    <td>{project.description}</td>
                                </tr>
                                <tr>
                                    <th>Technologies: </th>
                                    <td>{project.technologies.map((tech: ITechnologySimple) => (
                                        <React.Fragment>
                                            <Link to="/">{tech.name}</Link><br />
                                        </React.Fragment>
                                    ))}</td>
                                </tr>
                            </tbody>
                        </table>
                    </Card>
                    {project.consultants.length > 0 && (
                        <React.Fragment>
                            <h2>Consultants</h2>
                            <Row>
                                {project.consultants.map((consultant: IConsultantSimple) => (
                                    <Col s={12} m={6} l={4} xl={3}>
                                        <Card
                                            actions={[
                                                <Link 
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
                                            <h3>{consultant.fullname}</h3>
                                            <strong>{consultant.jobtitle}</strong>
                                        </Card>
                                    </Col>
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

export default ProjectDetail;
