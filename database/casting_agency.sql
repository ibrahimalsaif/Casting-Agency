--
-- PostgreSQL database dump
--

-- Dumped from database version 12.2
-- Dumped by pg_dump version 12.2

-- Started on 2020-08-09 07:13:45

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 205 (class 1259 OID 17095)
-- Name: actors ; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."actors " (
    id integer NOT NULL,
    name character varying,
    age integer,
    gender character varying
);


ALTER TABLE public."actors " OWNER TO postgres;

--
-- TOC entry 204 (class 1259 OID 17093)
-- Name: actors _id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."actors _id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."actors _id_seq" OWNER TO postgres;

--
-- TOC entry 2836 (class 0 OID 0)
-- Dependencies: 204
-- Name: actors _id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."actors _id_seq" OWNED BY public."actors ".id;


--
-- TOC entry 203 (class 1259 OID 17084)
-- Name: movies ; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."movies " (
    id integer NOT NULL,
    title character varying,
    release_date date
);


ALTER TABLE public."movies " OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 17082)
-- Name: movies _id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."movies _id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."movies _id_seq" OWNER TO postgres;

--
-- TOC entry 2837 (class 0 OID 0)
-- Dependencies: 202
-- Name: movies _id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."movies _id_seq" OWNED BY public."movies ".id;


--
-- TOC entry 2696 (class 2604 OID 17098)
-- Name: actors  id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."actors " ALTER COLUMN id SET DEFAULT nextval('public."actors _id_seq"'::regclass);


--
-- TOC entry 2695 (class 2604 OID 17087)
-- Name: movies  id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."movies " ALTER COLUMN id SET DEFAULT nextval('public."movies _id_seq"'::regclass);


--
-- TOC entry 2830 (class 0 OID 17095)
-- Dependencies: 205
-- Data for Name: actors ; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."actors " VALUES (1, 'Leonardo DiCaprio', 45, 'Male');
INSERT INTO public."actors " VALUES (2, 'Tom Hanks', 64, 'Male');
INSERT INTO public."actors " VALUES (3, 'Scarlett Johansson', 35, 'Female');
INSERT INTO public."actors " VALUES (4, 'Robert Downey Jr', 55, 'Male');
INSERT INTO public."actors " VALUES (5, 'Christian Bale', 46, 'Male');
INSERT INTO public."actors " VALUES (6, 'Matt Damon', 49, 'Male');
INSERT INTO public."actors " VALUES (7, 'Emma Roberts', 29, 'Female');
INSERT INTO public."actors " VALUES (8, 'Matthew McConaughey', 50, 'Male');
INSERT INTO public."actors " VALUES (9, 'Mahershala Ali', 46, 'Male');
INSERT INTO public."actors " VALUES (10, 'Woody Harrelson', 59, 'Male');


--
-- TOC entry 2828 (class 0 OID 17084)
-- Dependencies: 203
-- Data for Name: movies ; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."movies " VALUES (1, 'Good Will Hunting', '1997-12-02');
INSERT INTO public."movies " VALUES (2, 'The Dark Knight', '2008-07-14');
INSERT INTO public."movies " VALUES (3, 'Interstellar', '2014-10-26');
INSERT INTO public."movies " VALUES (4, 'Inception', '2010-08-13');
INSERT INTO public."movies " VALUES (5, 'The Hunger Games', '2012-03-12');
INSERT INTO public."movies " VALUES (6, 'Spider-Man', '2002-04-30');
INSERT INTO public."movies " VALUES (7, 'The Greatest Showman', '2017-12-08');
INSERT INTO public."movies " VALUES (8, 'Harry Potter and the Philosopher''s Stone', '2001-11-16');
INSERT INTO public."movies " VALUES (9, 'The Founder', '2016-11-24');
INSERT INTO public."movies " VALUES (10, 'Klaus', '2019-11-08');


--
-- TOC entry 2838 (class 0 OID 0)
-- Dependencies: 204
-- Name: actors _id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."actors _id_seq"', 10, true);


--
-- TOC entry 2839 (class 0 OID 0)
-- Dependencies: 202
-- Name: movies _id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."movies _id_seq"', 10, true);


--
-- TOC entry 2700 (class 2606 OID 17103)
-- Name: actors  actors _pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."actors "
    ADD CONSTRAINT "actors _pkey" PRIMARY KEY (id);


--
-- TOC entry 2698 (class 2606 OID 17092)
-- Name: movies  movies _pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."movies "
    ADD CONSTRAINT "movies _pkey" PRIMARY KEY (id);


-- Completed on 2020-08-09 07:13:46

--
-- PostgreSQL database dump complete
--

