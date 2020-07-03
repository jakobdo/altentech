import React, { useState, useEffect } from 'react';

import { IProject } from '../models/Project';
import API from '../utils/API';
import { Row, Col, Card, Chip } from 'react-materialize';
import { Link } from 'react-router-dom';
import { IConsultantSimple } from '../models/Consultant';
import { ITechnologySimple } from '../models/Technology';

function ProjectList(){
    const [projects, setProjects] = useState<IProject[]>([]);

    useEffect(() => {
        const fetchData = async() => {
            const result = await API.get('/projects/');
            setProjects(result.data);
        };
        fetchData();
    }, []);

    return (
        <div className="container">
            <h1>Projects</h1>
            <Row>
                {projects.map((project: IProject) => 
                    <Col s={12} m={6} l={4} key={project.slug}>
                        <Card
                            textClassName="center-align"
                        >
                            <h6>
                                <Link to={`/projects/${project.slug}`}>
                                    {project.name}
                                </Link>
                            </h6>
                            {(project.industry || project.client) && (
                                <strong>{project.client ? (
                                    project.client
                                ) : (
                                    project.industry
                                )}</strong>
                            )}
                       
                            <div className="left-align">{project.description}</div>
                            {project.consultants.length > 0 && (
                                <div className="left-align">
                                    <br />
                                    <strong>Consultants:</strong>
                                    {project.consultants.map((consultant: IConsultantSimple) => (
                                        <div key={consultant.slug}>
                                            <Link to={`/consultants/${consultant.slug}`}>
                                                {consultant.fullname}
                                            </Link>
                                        </div>
                                    ))}
                                </div>
                            )}
                            <br/>
                            {project.technologies.length > 0 && (
                                <div className="left-align">
                                    {project.technologies.map((technology: ITechnologySimple) => (
                                        <Link 
                                            to={`/technologies/${technology.slug}`}
                                            key={technology.slug}
                                        >
                                            <Chip>
                                                {technology.name}
                                            </Chip>
                                        </Link>
                                    ))}
                                </div>
                            )}
                        </Card>
                    </Col>
                )}
            </Row>
        </div>
    )
}

export default ProjectList;
