export interface IProject {
    pk: number;
    name: string;
    slug: string;
    description: string;
    client: number | null;
    industry: number | null;
    technologies: number[];
    consultants: number[];
}