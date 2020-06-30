import React, { useState, useEffect } from 'react';

import { IProject } from '../models/Project';
import API from '../utils/API';
import { Row, Col } from 'react-materialize';

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
                    <Col>{project.name}</Col>
                )}
            </Row>
        </div>
    )
}

export default ProjectList;
