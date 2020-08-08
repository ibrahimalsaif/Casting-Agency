--
-- PostgreSQL database dump
--

-- Dumped from database version 12.2
-- Dumped by pg_dump version 12.2

-- Started on 2020-08-07 19:59:35

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
-- TOC entry 205 (class 1259 OID 16915)
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
-- TOC entry 204 (class 1259 OID 16913)
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
-- TOC entry 203 (class 1259 OID 16904)
-- Name: movies ; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."movies " (
    id integer NOT NULL,
    title character varying,
    release_date date
);


ALTER TABLE public."movies " OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 16902)
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
-- TOC entry 2696 (class 2604 OID 16918)
-- Name: actors  id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."actors " ALTER COLUMN id SET DEFAULT nextval('public."actors _id_seq"'::regclass);


--
-- TOC entry 2695 (class 2604 OID 16907)
-- Name: movies  id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."movies " ALTER COLUMN id SET DEFAULT nextval('public."movies _id_seq"'::regclass);


--
-- TOC entry 2830 (class 0 OID 16915)
-- Dependencies: 205
-- Data for Name: actors ; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."actors " VALUES (1, 'Leonardo DiCaprio', 45, 'male');
INSERT INTO public."actors " VALUES (2, 'Will Smith', 51, 'male');
INSERT INTO public."actors " VALUES (3, 'Robert Downey', 55, 'male');
INSERT INTO public."actors " VALUES (4, 'Chris Hemsworth', 36, 'male');
INSERT INTO public."actors " VALUES (6, 'Dwayne Johnson', 50, 'male');


--
-- TOC entry 2828 (class 0 OID 16904)
-- Dependencies: 203
-- Data for Name: movies ; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."movies " VALUES (1, 'The Avengers', '2012-01-01');
INSERT INTO public."movies " VALUES (2, 'Iron Man', '2008-01-01');
INSERT INTO public."movies " VALUES (3, 'Thor ', '2011-01-01');
INSERT INTO public."movies " VALUES (4, 'Avengers: Infinity War', '2018-01-01');
INSERT INTO public."movies " VALUES (6, 'Jumanji: Welcome to the Jungle', '2018-05-12');


--
-- TOC entry 2838 (class 0 OID 0)
-- Dependencies: 204
-- Name: actors _id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."actors _id_seq"', 6, true);


--
-- TOC entry 2839 (class 0 OID 0)
-- Dependencies: 202
-- Name: movies _id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."movies _id_seq"', 6, true);


--
-- TOC entry 2700 (class 2606 OID 16923)
-- Name: actors  actors _pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."actors "
    ADD CONSTRAINT "actors _pkey" PRIMARY KEY (id);


--
-- TOC entry 2698 (class 2606 OID 16912)
-- Name: movies  movies _pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."movies "
    ADD CONSTRAINT "movies _pkey" PRIMARY KEY (id);


-- Completed on 2020-08-07 19:59:35

--
-- PostgreSQL database dump complete
--

