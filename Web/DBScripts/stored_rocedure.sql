-- ---------------------------------------------------------------


DROP FUNCTION public.fn_enquiry_search(text, text, text, text, boolean, text, text, integer, integer, integer, integer);

CREATE OR REPLACE FUNCTION public.fn_enquiry_search(
	denquiry_type text,
	dfiltertype text,
	dstartdate text,
	denddate text,
	discompleted boolean,
	dcategoryids text,
	dsearchtext text,
	disadmin integer,
	duserid integer,
	dpage integer,
	drow integer)
    RETURNS TABLE(public_id text, plan_id integer, email text, ic_no text, contact_no text, company_name text, brn_no text, contact_person_name text, due_date text, assigned_to integer, appointment_date text, status integer, plan_name text, category_id integer, isactive integer, employer_name text, full_count bigint, phone_name text, enquiry_type text, phone_public_id text) 
    LANGUAGE 'sql'

    COST 100
    VOLATILE 
    ROWS 1000
AS $BODY$

    SELECT  te.public_id, plan_id, email, ic_no, contact_no, 
	company_name, brn_no, contact_person_name, to_char(due_date,'MM-DD-YYYY HH24:MI:SS'), 
	assigned_to,to_char(appointment_date,'MM-DD-YYYY HH24:MI:SS') , status,tp.plan_name,category_id,
	te."isActive",employer_name,count(*) OVER() AS full_count,tph.phone_name,te.enquiry_type,tph.public_id as phone_public_id
	FROM public.tblenquiry te
	left join tblplans tp on tp.id=te.plan_id
	left join tblphone tph on tph.id=te.phone_id
	where case when dfiltertype='due' and nullif(dstartdate,'')<>'' then  date(due_date)>=to_date(dstartdate,'mm-dd-yyyy') else true end  and
          case when dfiltertype='due' and nullif(denddate,'')<>'' then  date(due_date)<=to_date(denddate,'mm-dd-yyyy') else true end and
		  case when dfiltertype='appointment' and nullif(dstartdate,'')<>'' then  date(appointment_date)>=to_date(dstartdate,'mm-dd-yyyy') else true end and
          case when dfiltertype='appointment' and nullif(denddate,'')<>'' then  date(appointment_date)<=to_date(denddate,'mm-dd-yyyy') else true end and
		  case when discompleted<>true then status<>100 else status=100 end and
		  case when  nullif(dcategoryids,'')<>'' then category_id = ANY (string_to_array(dcategoryids, ',')::int[]) else true end and
		  case when  nullif(dsearchtext,'')<>''  then company_name ILIKE dsearchtext 
		    or  contact_person_name ILIKE dsearchtext  or  brn_no ILIKE dsearchtext 
			or  ic_no ILIKE dsearchtext or tph.phone_name ILIKE dsearchtext or tp.plan_name ILIKE dsearchtext  or  email ILIKE dsearchtext  or contact_no LIKE dsearchtext
		   else true end  and  te."isActive"=1 and
		   case when  nullif(denquiry_type,'')<>'' then te.enquiry_type=denquiry_type else true end and
		   case when disadmin<>1 then te.created_by=duserid or assigned_to=duserid else true end LIMIT drow OFFSET (dpage-1)*drow;
	
$BODY$;


-- ---------------------------------------------------------------

-- ---------------------------------------------------------------

-- ---------------------------------------------------------------

-- ---------------------------------------------------------------

-- ---------------------------------------------------------------

-- ---------------------------------------------------------------

-- ---------------------------------------------------------------