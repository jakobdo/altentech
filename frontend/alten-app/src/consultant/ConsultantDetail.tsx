import React, { useState, useEffect } from 'react';

import { IConsultant } from '../models/Consultant';
import API from '../utils/API';
import { Row, Col, Card, Icon } from 'react-materialize';
import { useParams, Link } from 'react-router-dom';
import Loading from '../common/Loading';
import TechnologyLevels from '../common/TechnologyLevels';
import {IProjectSimple} from '../models/Project';
import { ITechnologySimple } from '../models/Technology';
import TechSeparator from '../common/TechSeparator';
import { IExperience } from '../models/Experience';

import './ConsultantDetail.css';

function ConsultantDetail(){
    const { consultantSlug } = useParams();
    const [consultant, setConsultant] = useState<IConsultant | null>(null);

    useEffect(() => {
        const fetchConsultant = async() => {
            const result = await API.get(`/consultants/${consultantSlug}/`);
            setConsultant(result.data);
        };
        fetchConsultant();
    }, [consultantSlug]);

    const mailSubject = consultant ? encodeURI(`Book consultant - ${consultant.fullname}`) : '';

    return (
        <div className="container">
            {consultant ? (
                <React.Fragment>
                    <Card>
                        <div className="center-align">
                            <img className="circle responsive-img" src={consultant.image.medium} alt={consultant.fullname} />
                        </div>
                        <div className="center-align">
                            <h1>{consultant.fullname}</h1>
                            <h2>{consultant.jobtitle}</h2>
                            <hr />
                        </div>
                        <div className="left-align">{consultant.description}</div>
                        <Row className="center-align">
                            <Col s={6}>
                                <a
                                    href={`mailto:tech@alten.dk?subject=${mailSubject}`}
                                    className="waves-effect waves-light btn"
                                >
                                    <Icon left={true}>schedule</Icon>Book Consultant
                                </a>
                            </Col>
                            <Col s={6}>
                                <a
                                    href={consultant.cv}
                                    className="waves-effect waves-light btn"
                                    target="_blank"
                                    rel="noopener noreferrer"
                                >
                                    <Icon left={true}>file_download</Icon>Download CV
                                </a>
                            </Col>
                        </Row>
                        {consultant.linkedin && (
                            <div className="center-align">
                                <a 
                                    href={consultant.linkedin}
                                    target="_blank"
                                    rel="noopener noreferrer">
                                        <img src="http://localhost:8000/static/base/logo/linkedin.png" alt="LinkedIn" />
                                </a>
                            </div>
                        )}
                    </Card>

                    {consultant.technologyLevels.length > 0 && (
                        <React.Fragment>
                            <div className="center-align">
                                <Icon>star</Icon>
                            </div>

                            <Card>
                                <h2 className="center-align">Technologies & Tools</h2>
                                <TechnologyLevels technologyLevels={consultant.technologyLevels} />
                            </Card>
                        </React.Fragment>
                    )}

                    {consultant.projects.length > 0 && (
                        <React.Fragment>
                            <div className="center-align">
                                <Icon>group_work</Icon>
                            </div>

                            <Card>
                                <h2 className="center-align">Projects</h2>
                                {consultant.projects.map((project: IProjectSimple) => (
                                    <React.Fragment key={project.slug}>
                                        <Link to={`/projects/${project.slug}/`}>{project.name}</Link> : 
                                        <React.Fragment>
                                            {project.technologies.map<React.ReactNode>((technology: ITechnologySimple) => (
                                                <Link to={`/technologies/${technology.slug}/`}>{technology.name}</Link>
                                            )).reduce((prev, curr) => [prev, <TechSeparator />, curr])}
                                        </React.Fragment>
                                    </React.Fragment>
                                ))}
                            </Card>
                        </React.Fragment>
                    )}

                    {consultant.experience.length > 0 && (
                        <React.Fragment>
                            <div className="center-align">
                                <Icon>work</Icon>
                            </div>

                            <Card>
                                <h2 className="center-align">Experience</h2>
                                <div className="timeline">
                                    {consultant.experience.map((job: IExperience) => (
                                        <div className="timeline-event">
                                            <div className="card timeline-content alten-light-blue">
                                                <div className="card-content">
                                                    <span className="card-title alten-header-color">{job.start} - {job.company}</span>
                                                    <p className="alten-p-light-blue"><b>{job.job_title}</b></p>
                                                    <hr />
                                                    <p>{job.description}</p>
                                                </div>
                                            </div>
                                            <div className="timeline-badge blue white-text">
                                                <i className="material-icons">my_location</i>
                                            </div>
                                        </div>
                                    ))}
                                </div>
                            </Card>
                        </React.Fragment>
                    )}
                </React.Fragment>
            ) : (
                <Loading />
            )}
            
        </div>
    )
}

export default ConsultantDetail;
